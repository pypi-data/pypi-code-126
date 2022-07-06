"""
Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from abc import abstractmethod, ABC

from sweetpotato.authentication import AuthenticationProvider
from sweetpotato.components import SafeAreaProvider
from sweetpotato.config import settings
from sweetpotato.core.protocols import Composite
from sweetpotato.navigation import NavigationContainer
from sweetpotato.ui_kitten import ApplicationProvider


class Wrapper(ABC):
    """Wrapping interface for components."""

    @abstractmethod
    def wrap(self, component, **kwargs) -> Composite:
        return component


class UIKittenWrapper(Wrapper):
    """Adds UI Kitten support to app.

    Todo:
        * Replace general exception with custom exception.
    """

    def wrap(self, component: Composite, **kwargs) -> Composite:
        """Wraps component in UI Kitten if enabled.

        Args:
            component (Composite): ...

        Returns:
            Composite.
        """
        if settings.USE_UI_KITTEN:
            theme = kwargs.pop("theme", None)
            if not theme:
                raise Exception("UI Kitten must be provided a theme.")
            component = ApplicationProvider(
                children=[component], theme=f"{'{'}...eva.{theme}{'}'}"
            )
        return super().wrap(component, **kwargs)


class AuthenticationWrapper(Wrapper):
    """Adds authentication plugins to app.

    Todo:
        * Add docstrings.
    """

    def wrap(self, component: Composite, **kwargs) -> Composite:
        if settings.USE_AUTHENTICATION:
            component = AuthenticationProvider(children=[component])
        return super().wrap(component, **kwargs)


class NavigationWrapper(Wrapper):
    """Adds NavigationContainer component to app and gives navigation capability.

    Todo:
        * Add docstrings.
    """

    def wrap(self, component: Composite, **kwargs) -> Composite:
        if settings.USE_NAVIGATION:
            component = NavigationContainer(
                children=[component], ref="RootNavigation.navigationRef"
            )
        return super().wrap(component, **kwargs)


class SafeAreaWrapper(Wrapper):
    """Adds react-native-safe-area-context SafeAreaProvider component to app.


    Todo:
        * Add docstrings
    """

    def wrap(self, component, **kwargs) -> Composite:
        component = SafeAreaProvider(children=[component])
        return super().wrap(component, **kwargs)


class ContextWrapper(
    AuthenticationWrapper, SafeAreaWrapper, UIKittenWrapper, NavigationWrapper
):
    """Checks for and adds navigation, authentication, and ui-kitten contexts.


    Todo:
        * Add docstrings
    """

    def wrap(self, component: list, **kwargs) -> Composite:
        component = super().wrap(component[0], **kwargs)
        component.is_root = True
        return component
