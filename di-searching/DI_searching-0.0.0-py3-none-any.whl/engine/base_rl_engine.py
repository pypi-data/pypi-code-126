import numpy as np
from typing import Any, Dict, Callable, List, Optional, Tuple

from .base_search_engine import BaseSearchEngine, ENGINE_REGISTRY
from disearch.problem import ProblemEnv
from ding.utils import deep_merge_dicts
from ding.worker import BaseLearner, SampleSerialCollector


class BaseRLEngine(BaseSearchEngine):

    config = dict(
        samples_per_iteration=128,
        max_iterations=100,
        env=dict(),
        policy=dict(collect=dict(collector=dict(), ), learn=dict(learner=dict(), )),
    )

    def __init__(
            self,
            cfg: Dict,
            search_space: "BaseSpace",  # noqa
            policy,
    ) -> None:
        cfg.policy.collect.collector = deep_merge_dicts(
            SampleSerialCollector.default_config(), cfg.policy.collect.collector
        )
        cfg.policy.learn.learner = deep_merge_dicts(BaseLearner.default_config(), cfg.policy.learn.learner)
        super().__init__(cfg, search_space)

        self._policy = policy
        self._collector = None
        self._learner = BaseLearner(cfg.policy.learn.learner, self._policy.learn_mode)
        self._replay_buffer = None
        self._best = None

        self._max_iterations = self._cfg.max_iterations
        self._samples_per_iteration = self._cfg.samples_per_iteration

    def reset(self) -> None:
        self._collector = None

    def propose(self, candidate_num: int) -> np.ndarray:
        new_data = self._collector.collect(candidate_num, train_iter=self._learner.train_iter)
        return new_data

    def search(self, target_func: Callable) -> Tuple[np.ndarray, int]:
        env = ProblemEnv(self._cfg.env, self._search_space, target_func)
        env.set_episode_len(self._samples_per_iteration // env.env_num)
        if self._collector is None:
            self._collector = SampleSerialCollector(self._cfg.policy.collect.collector, env, self._policy.collect_mode)
        else:
            self._collector.reset_env(env)

        for i in range(self._max_iterations):
            new_data = self.propose(self._samples_per_iteration)
            self.update_score(new_data)
            self._best = env.best
        return self.provide_best()

    def update_score(self, train_data: List) -> None:
        if self._replay_buffer is not None:
            self._replay_buffer.push(train_data, cur_collector_envstep=self._collector.envstep)
            for j in range(self._cfg.policy.learn.update_per_collect):
                train_data = self._replay_buffer.sample(self._cfg.policy.learn.batch_size, self._learner.train_iter)
                self._learner.train(train_data, self._collector.envstep)
            if self._learner.policy.get_attribute('priority'):
                self._replay_buffer.update(self._learner.priority_info)
        else:
            self._learner.train(train_data, self._collector.envstep)

    def provide_best(self) -> Tuple[np.ndarray, np.ndarray]:
        return self._best
