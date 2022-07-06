# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)
from ..models import User
from ..utils.exceptions import (
    AddComponentError,
    GetComponentError,
    UpdateComponentError,
)
from .base import ComponentBase


class Users(ComponentBase):

    """Used to sync users from a source instance to a destination instance of Swimlane."""

    def _process_user(self, user: User):
        """Processes roles and groups associated with a source Swimlane instance `User` object.

        Attempts to make sure that roles and groups are created on the Swimlane destination instance.

        Args:
            user (User): A source Swimlane instance `User` object.

        Returns:
            User: A modified source Swimlane instance `User` object.
        """
        if user.roles:
            self.log(f"Processing roles for user '{user.name}'")
            role_list = []
            from .roles import Roles

            for role in user.roles:
                _role = Roles().sync_role(role=role)
                if _role:
                    role_list.append(_role)
            user.roles = role_list
        if user.groups:
            self.log(f"Processing groups for user '{user.name}'")
            group_list = []
            from .groups import Groups

            for group in user.groups:
                _group = Groups().sync_group(group=group)
                if _group:
                    group_list.append(_group)
            user.groups = group_list
        return user

    def sync_user(self, user_id):
        """Syncs a single source Swimlane instance user with a destination instance.

        Args:
            user_id (str): A Swimlane user ID.

        Raises:
            GetComponentError: Raises when the provided user_id is not found on the source Swimlane instance.
            AddComponentError: Raises when unable to add a user to a destination Swimlane instance.
            UpdateComponentError: Raises when unable to update a user on a destination Swimlane instance.

        Returns:
            User: A destination Swimlane instance `User` object.
        """
        user = self.source_instance.get_user(user_id)
        if not user:
            raise GetComponentError(type="User", id=user_id)
        self.log(f"Processing user '{user.displayName}' ({user_id})")
        if user and not self._is_in_include_exclude_lists(user.displayName, "users"):
            if (
                user.displayName != self.source_instance.swimlane.user.display_name
                or user.userName != self.source_instance.swimlane.user.username
            ):
                self.log(f"Attempting to sync user '{user.displayName}' on destination.")
                dest_user = self.destination_instance.search_user(user.userName)
                if not dest_user:
                    if not ComponentBase.dry_run:
                        self.log(f"Adding new user '{user.displayName}' to destination.")
                        dest_user = self.destination_instance.add_user(user)
                        if not dest_user:
                            raise AddComponentError(model=user, name=user.displayName)
                        self.log(f"Successfully added user '{user.displayName}' to destination.")
                        return dest_user
                    else:
                        self.add_to_diff_log(user.displayName, "added")
                else:
                    self.log(f"User '{user.displayName}' exists on destination.")
                    user = self._process_user(user=user)
                    if not ComponentBase.dry_run:
                        user.id = dest_user.id
                        dest_user = self.destination_instance.update_user(dest_user.id, user)
                        if not dest_user:
                            raise UpdateComponentError(model=user, name=user.displayName)
                        self.log(f"Successfully updated user '{user.displayName}' on destination.")
                        return dest_user
                    else:
                        self.add_to_diff_log(user.displayName, "updated")
            else:
                dname = self.source_instance.swimlane.user.display_name
                self.log(f"Unable to update the currently authenticated user '{dname}'. Skipping...")

    def sync(self):
        """This method is used to sync all users from a source instance to a destination instance."""
        self.log(f"Attempting to sync users from '{self.source_host}' to '{self.dest_host}'.")
        users = self.source_instance.get_users()
        if users:
            for user in users:
                self.sync_user(user_id=user.id)
        self.log(f"Completed syncing of users from '{self.source_host}' to '{self.dest_host}'.")
