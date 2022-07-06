"""Module that contains a patch for the zerorpc"""
import gc
from zerorpc import Event
from zerorpc import core, context, events
import cloudpickle as pickle

PROTOCOL = 4  # The highest available in Python 3.6


def pack(self):
    gc.disable()
    payload = (self._header, self._name, self._args)
    serialized = pickle.dumps(payload, protocol=PROTOCOL)
    gc.enable()
    return serialized


def unpack(blob: memoryview):
    gc.disable()
    unpacked_msg = pickle.loads(blob.tobytes())
    try:
        (header, name, args) = unpacked_msg
    except Exception as e:
        raise Exception('invalid msg format "{0}": {1}'.format(unpacked_msg, e))

    # Backward compatibility
    if not isinstance(header, dict):
        header = {}
    gc.enable()

    # print(f"Unpacking {size} bytes in {time.time() - start}s [{unpacked_msg}]")
    return Event(name, args, None, header)


from future.utils import tobytes

import uuid
import random
from zmq import green as zmq


class Context(zmq.Context):
    _instance = None

    def __init__(self):
        """init function"""
        super(zmq.Context, self).__init__()
        self._middlewares = []
        self._hooks = {
            "resolve_endpoint": [],
            "load_task_context": [],
            "get_task_context": [],
            "server_before_exec": [],
            "server_after_exec": [],
            "server_inspect_exception": [],
            "client_handle_remote_error": [],
            "client_before_request": [],
            "client_after_request": [],
            "client_patterns_list": [],
        }
        self._reset_msgid()

    # NOTE: pyzmq 13.0.0 messed up with setattr (they turned it into a
    # non-op) and you can't assign attributes normally anymore, hence the
    # tricks with self.__dict__ here

    @property
    def _middlewares(self):
        return self.__dict__["_middlewares"]

    @_middlewares.setter
    def _middlewares(self, value):
        self.__dict__["_middlewares"] = value

    @property
    def _hooks(self):
        return self.__dict__["_hooks"]

    @_hooks.setter
    def _hooks(self, value):
        self.__dict__["_hooks"] = value

    @property
    def _msg_id_base(self):
        return self.__dict__["_msg_id_base"]

    @_msg_id_base.setter
    def _msg_id_base(self, value):
        self.__dict__["_msg_id_base"] = value

    @property
    def _msg_id_counter(self):
        return self.__dict__["_msg_id_counter"]

    @_msg_id_counter.setter
    def _msg_id_counter(self, value):
        self.__dict__["_msg_id_counter"] = value

    @property
    def _msg_id_counter_stop(self):
        return self.__dict__["_msg_id_counter_stop"]

    @_msg_id_counter_stop.setter
    def _msg_id_counter_stop(self, value):
        self.__dict__["_msg_id_counter_stop"] = value

    @staticmethod
    def get_instance():
        if Context._instance is None:
            Context._instance = Context()
        return Context._instance

    def _reset_msgid(self):
        self._msg_id_base = tobytes(uuid.uuid4().hex)[8:]
        self._msg_id_counter = random.randrange(0, 2 ** 32)
        self._msg_id_counter_stop = random.randrange(self._msg_id_counter, 2 ** 32)

    def new_msgid(self):
        if self._msg_id_counter >= self._msg_id_counter_stop:
            self._reset_msgid()
        else:
            self._msg_id_counter = self._msg_id_counter + 1
        return tobytes("{0:08x}".format(self._msg_id_counter)) + self._msg_id_base

    def register_middleware(self, middleware_instance):
        registered_count = 0
        self._middlewares.append(middleware_instance)
        for hook in self._hooks:
            functor = getattr(middleware_instance, hook, None)
            if functor is None:
                try:
                    functor = middleware_instance.get(hook, None)
                except AttributeError:
                    pass
            if functor is not None:
                self._hooks[hook].append(functor)
                registered_count += 1
        return registered_count

    #
    # client/server
    #
    def hook_resolve_endpoint(self, endpoint):
        for functor in self._hooks["resolve_endpoint"]:
            endpoint = functor(endpoint)
        return endpoint

    def hook_load_task_context(self, event_header):
        for functor in self._hooks["load_task_context"]:
            functor(event_header)

    def hook_get_task_context(self):
        event_header = {}
        for functor in self._hooks["get_task_context"]:
            event_header.update(functor())
        return event_header

    #
    # Server-side hooks
    #
    def hook_server_before_exec(self, request_event):
        """Called when a method is about to be executed on the server."""

        for functor in self._hooks["server_before_exec"]:
            functor(request_event)

    def hook_server_after_exec(self, request_event, reply_event):
        """Called when a method has been executed successfully.

        This hook is called right before the answer is sent back to the client.
        If the method streams its answer (i.e: it uses the zerorpc.stream
        decorator) then this hook will be called once the reply has been fully
        streamed (and right before the stream is "closed").

        The reply_event argument will be None if the Push/Pull pattern is used.

        """
        for functor in self._hooks["server_after_exec"]:
            functor(request_event, reply_event)

    def hook_server_inspect_exception(self, request_event, reply_event, exc_infos):
        """Called when a method raised an exception.

        The reply_event argument will be None if the Push/Pull pattern is used.

        """
        task_context = self.hook_get_task_context()
        for functor in self._hooks["server_inspect_exception"]:
            functor(request_event, reply_event, task_context, exc_infos)

    #
    # Client-side hooks
    #
    def hook_client_handle_remote_error(self, event):
        exception = None
        for functor in self._hooks["client_handle_remote_error"]:
            ret = functor(event)
            if ret:
                exception = ret
        return exception

    def hook_client_before_request(self, event):
        """Called when the Client is about to send a request.

        You can see it as the counterpart of ``hook_server_before_exec``.

        """
        for functor in self._hooks["client_before_request"]:
            functor(event)

    def hook_client_after_request(self, request_event, reply_event, exception=None):
        """Called when an answer or a timeout has been received from the server.

        This hook is called right before the answer is returned to the client.
        You can see it as the counterpart of the ``hook_server_after_exec``.

        If the called method was returning a stream (i.e: it uses the
        zerorpc.stream decorator) then this hook will be called once the reply
        has been fully streamed (when the stream is "closed") or when an
        exception has been raised.

        The optional exception argument will be a ``RemoteError`` (or whatever
        type returned by the client_handle_remote_error hook) if an exception
        has been raised on the server.

        If the request timed out, then the exception argument will be a
        ``TimeoutExpired`` object and reply_event will be None.

        """
        for functor in self._hooks["client_after_request"]:
            functor(request_event, reply_event, exception)

    def hook_client_patterns_list(self, patterns):
        for functor in self._hooks["client_patterns_list"]:
            patterns = functor(patterns)
        return patterns


def monkey_patch():
    # print("Monkey patching ZeroRPC")
    Event.pack = pack
    Event.unpack = unpack

    context.zmq = zmq
    context.Context = Context
    core.zmq = zmq
    events.zmq = zmq
