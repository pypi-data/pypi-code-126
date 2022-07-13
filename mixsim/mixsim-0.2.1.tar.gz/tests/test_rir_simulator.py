# import unittest
# from pathlib import Path
#
# import librosa
# import numpy as np
#
# from mixsim.rir_simulator.base_rir_simulator import BaseRIRSimulator, Source
# from mixsim.rir_simulator.source import Microphone
#
#
# class TestSource(unittest.TestCase):
#     def test_static_source(self):
#         static_source = Source(y=np.array([0]))
#         static_source.traj = np.array([[0, 0, 0]])
#         dynamic_source = Source(y=np.array([0]))
#         dynamic_source.traj = np.array([[0, 0, 0], [1, 1, 1]])
#         assert static_source.is_static is True
#         assert dynamic_source.is_static is False
#
#
# class TestRIRSimulator(unittest.TestCase):
#     print("Loading audio...")
#     audio, sr = librosa.load("notebooks/assets/clean.wav", sr=16000)
#     print(f"audio with the shape of {audio.shape}")
#     room = Room(size=np.array([5, 5, 5]), abs_weights=np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5]), rt60=0.5)
#     mic = Microphone(mic_position=np.array([[3, 2, 3]]))  # [num_mics, dim] = [1, 3]
#     source = Source(y=audio, sr=sr)  # [num_traj, dim] = [1, 3]
#     source.traj = np.array([[3, 4, 3]])
#     simulator = BaseRIRSimulator()
#
#     def test_simulate_rir_one_source_one_mic(self) -> None:
#         print("Simulating RIR...")
#         self.simulator.simulate_rirs(
#             room=self.room,
#             microphone=self.mic,
#             sources=[
#                 self.source,
#             ],
#         )
#         assert self.source.y_rvb is not None
#         print(self.source.y_rvb.shape)
#
#     def test_simulate_rir_one_source_multiple_mics(self) -> None:
#         print("Simulating RIR...")
#         self.mic = Microphone(mic_position=np.array([[3, 2, 3], [3, 4, 3]]))  # [num_mics, dim] = [2, 3]
#         self.simulator.simulate_rirs(
#             room=self.room,
#             microphone=self.mic,
#             sources=[
#                 self.source,
#             ],
#         )
#         assert self.source.y_rvb is not None
#         print(self.source.y_rvb.shape)
#
#     def test_simulate_rir_multiple_dynamic_sources_multiple_mic(self) -> None:
#         print("Simulating RIR...")
#         source_1 = Source(y=self.audio, sr=self.sr)
#         source_1.traj = np.array([[3, 4, 3], [3, 2, 3]])
#         source_2 = Source(y=self.audio, sr=self.sr)
#         source_2.traj = np.array([[3, 2, 3], [3, 4, 3]])
#         self.mic = Microphone(mic_position=np.array([[3, 2, 3], [3, 4, 3]]))  # [num_mics, dim] = [2, 3]
#         self.simulator.simulate_rirs(
#             room=self.room,
#             microphone=self.mic,
#             sources=[source_1, source_2],
#         )
#         assert source_1.y_rvb is not None
#         assert source_2.y_rvb is not None
#         print(source_1.y_rvb.shape)
#         print(source_2.y_rvb.shape)
