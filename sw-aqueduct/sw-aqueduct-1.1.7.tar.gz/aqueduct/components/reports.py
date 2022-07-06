# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)
from ..models import Report
from ..utils.exceptions import AddComponentError
from .base import ComponentBase


class Reports(ComponentBase):

    """Used to sync reports from a source instance to a destination instance of Swimlane."""

    def _update_destination_report(self, source: Report, destination: Report, application_name=None):
        """Updates the destination report with values missing from the source report.

        Args:
            source (Report): Source Swimlane instance report.
            destination (Report): Destination Swimlane instance report.
            application_name (str, optional): Swimlane application name used for logging. Defaults to None.

        Returns:
            Report: Updated destination Swimlane instance `Report` object.
        """
        if source.columns and destination.columns and source.columns != destination.columns:
            for scolumn in source.columns:
                if scolumn not in destination.columns:
                    if ComponentBase.dry_run:
                        self.add_to_diff_log(
                            f"{application_name if application_name else ''} - {destination.name} Report",
                            "updated",
                            subcomponent="columns",
                        )
                    else:
                        self.log(f"Report '{destination.name}' does not contain column '{scolumn}'. Adding now.")
                    destination.columns.append(scolumn)
        if source.filters and not destination.filters:
            for sfilter in source.filters:
                if sfilter not in destination.filters:
                    if ComponentBase.dry_run:
                        self.add_to_diff_log(
                            f"{application_name if application_name else ''} - {destination.name} Report",
                            "updated",
                            subcomponent="filters",
                        )
                    else:
                        self.log(f"Report '{destination.name}' does not contain filter '{sfilter}'. Adding now.")
                    destination.filters.append(sfilter)
        if source.keywords and not destination.keywords:
            if ComponentBase.dry_run:
                self.add_to_diff_log(
                    f"{application_name if application_name else ''} - {destination.name} Report",
                    "updated",
                    subcomponent="keywords",
                )
            else:
                self.log(f"Report '{destination.name}' does not contain keywords '{source.keywords}'. Adding now.")
            destination.keywords = source.keywords
        return destination

    def _update_default_report(self, sreport: Report, dreport: Report):
        """Used to update a "Default" report on a destination Swimlane instance.

        Args:
            sreport (Report): A source Swimlane instance `Report` object.
            dreport (Report): A destination Swimlane instance `Report` object.

        Returns:
            Report: A modified destination Swimlane instance `Report` object.
        """
        self.log("Updating 'Default' report.")
        dest_application = self.destination_instance.get_application(sreport.applicationIds[0])
        if dest_application:
            self.log(
                f"Getting source default report and application for application ID '{sreport.applicationIds[0]}'",
                level="debug",
            )
            source_default_report = self.source_instance.get_default_report_by_application_id(sreport.applicationIds[0])
            source_application = self.source_instance.get_application(sreport.applicationIds[0])

            self.log(
                f"Getting destination application '{dest_application['name']}' Tracking ID field ID",
                level="debug",
            )
            dest_tracking_field = None
            for field in dest_application.get("fields"):
                if field.get("fieldType") and field["fieldType"].lower() == "tracking":
                    dest_tracking_field = field.get("id")
            self.log(
                f"Destination application '{dest_application['name']}' Tracking ID field ID is '{dest_tracking_field}'",
                level="debug",
            )
            self.log(
                f"Getting source application '{source_application['name']}' Tracking ID field ID",
                level="debug",
            )
            source_tracking_field = None
            for field in source_application.get("fields"):
                if field.get("fieldType") and field["fieldType"].lower() == "tracking":
                    source_tracking_field = field.get("id")
            self.log(
                f"Source application '{source_application['name']}' Tracking ID field ID is '{source_tracking_field}'",
                level="debug",
            )

            if source_tracking_field in source_default_report.columns:
                self.log(
                    "Updating columns in default report to match tracking IDs",
                    level="debug",
                )
                source_default_report.columns.remove(source_tracking_field)
                source_default_report.columns.append(dest_tracking_field)
                if ComponentBase.dry_run:
                    self.add_to_diff_log(
                        f"{dest_application['name']} - Default Report",
                        "updated",
                        subcomponent="tracking-id",
                    )

            if source_default_report.sorts and source_default_report.sorts.get(source_tracking_field):
                self.log(
                    "Updating sorts in default report to match tracking IDs",
                    level="debug",
                )
                val = source_default_report.sorts[source_tracking_field]
                source_default_report.sorts.pop(source_tracking_field)
                source_default_report.sorts.update({dest_tracking_field: val})
                if ComponentBase.dry_run:
                    self.add_to_diff_log(
                        f"{dest_application['name']} - Default Report",
                        "updated",
                        subcomponent="sorts",
                    )
            self.log("Updating default report id, uid, and version strings.", level="debug")
            source_default_report.id = dreport.id
            if ComponentBase.dry_run:
                self.add_to_diff_log(
                    f"{dest_application['name']} - Default Report",
                    "updated",
                    subcomponent="id",
                )
            source_default_report.uid = dreport.uid
            if ComponentBase.dry_run:
                self.add_to_diff_log(
                    f"{dest_application['name']} - Default Report",
                    "updated",
                    subcomponent="uid",
                )
            source_default_report.version = dreport.version
            if ComponentBase.dry_run:
                self.add_to_diff_log(
                    f"{dest_application['name']} - Default Report",
                    "updated",
                    subcomponent="version",
                )
            return self._update_destination_report(
                source=source_default_report,
                destination=dreport,
                application_name=dest_application["name"],
            )
        else:
            self.log(
                f"Unable to update 'Default' report for application ID '{sreport.applicationIds[0]}'"
                " because that ID does not exist on destination.",
                level="warning",
            )

    def sync_report(self, report: Report):
        """This method syncs a single Swimlane source `Report` object.

        This method has two branches of processing. The first checks to see if the report is a "Default" report.

            If a report is a "Default" report (e.g. the record view report) then we first attempt to retrieve the
            associated application's default report by it's ID. If that report is not found then we attempt to
            retrieve the report the normal way.

            If we were able to retrieve the report and `update_reports` was set to `True` then we process the default
            report in the update_default_report method (see docs on that method for details). Finally, after processing
            that report we update it on the destination instance.

            If we are NOT able to retrieve the report then we add the report to the destination instance.

        If the report is NOT a "Default" report then we process it like most other components.

            We first check to see if the destination instance has the report. If the report is NOT found on the
            destination then we add the report.

            If the report is found on the destination and `update_reports` was set to `True` then we process the report
            by updating different pieces of the report that are missing from the destination instance.

        Args:
            report (Report): A source Swimlane instance `Report` object.

        Raises:
            AddComponentError: Raises when we are unable to add a Report object to the destination instance.
        """
        self.log(f"Processing report '{report.name}' ({report.id})")
        if not self._is_in_include_exclude_lists(report.name, "reports"):
            if report.name == "Default":
                self.log(f"Checking for 'Default' report for application ID '{report.applicationIds[0]}'")
                default_report = self.destination_instance.get_default_report_by_application_id(
                    report.applicationIds[0]
                )
                if not default_report:
                    default_report = self.destination_instance.get_report(report_id=report.id)
                if default_report:
                    if self.update_reports:
                        if not ComponentBase.dry_run:
                            self.log(f"Destination report '{report.name}' has changes that source does not.")
                            dest_report = self._update_default_report(sreport=report, dreport=default_report)
                            resp = self.destination_instance.update_default_report(dest_report)
                            self.log("Successfully updated 'Default' report.")
                        else:
                            self.add_to_diff_log(report.name, "updated")
                    else:
                        self.log(
                            "Default report was found. If you want to update the default report use"
                            " update_reports=True. Skipping..."
                        )
                else:
                    if not ComponentBase.dry_run:
                        self.log(
                            f"Report '{report.name}' for application IDs '{report.applicationIds}' was not found on"
                            " destination. Adding report..."
                        )
                        resp = self.destination_instance.add_report(report)
                        if not resp:
                            raise AddComponentError(model=report, name=report.name)
                        self.log(f"Successfully added report '{report.name}' to destination.")
                    else:
                        self.add_to_diff_log(report.name, "added")
            else:
                dest_report = self.destination_instance.get_report(report_id=report.id)
                if not dest_report:
                    if not ComponentBase.dry_run:
                        self.log(
                            f"Report '{report.name}' for application IDs '{report.applicationIds}' was not found on"
                            " destination. Adding report..."
                        )
                        resp = self.destination_instance.add_report(report)
                        if not resp:
                            raise AddComponentError(model=report, name=report.name)
                        self.log(f"Successfully added report '{report.name}' to destination.")
                    else:
                        self.add_to_diff_log(report.name, "added")
                elif self.update_reports:
                    self.log(
                        f"Report '{report.name}' for application IDs '{report.applicationIds}' was found."
                        " Checking difference...."
                    )
                    if report != dest_report:
                        if not ComponentBase.dry_run:
                            self.log("Source and destination report are different. Updating ...")
                            dest_report = self._update_destination_report(source=report, destination=dest_report)
                            self.destination_instance.update_report(report.id, dest_report)
                            self.log(f"Successfully updated report '{report.name}' on destination.")
                        else:
                            self.add_to_diff_log(report.name, "updated")
                    else:
                        self.log(f"No differences found in report '{report.name}'. Skipping...")
                else:
                    self.log(f"Skipping check of report '{report.name}' for changes since update_reports is False.")

    def sync(self):
        """This method is used to sync all reports from a source instance to a destination instance."""
        self.log(f"Attempting to sync reports from '{self.source_host}' to '{self.dest_host}'.")
        reports = self.source_instance.get_reports()
        if reports:
            for report in reports:
                self.sync_report(report=report)
        self.log(f"Completed syncing of reports from '{self.source_host}' to '{self.dest_host}'.")
