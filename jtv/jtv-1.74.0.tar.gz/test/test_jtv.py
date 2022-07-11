# test_jtv.py
import pytest
from click.testing import CliRunner
from jtv.cli import cli
from command_io import *


@pytest.fixture
def runner():
  return CliRunner()


def test_no_args(runner):
  result = runner.invoke(cli)
  assert result.exit_code == 0
  assert result.output == jtv_help


def test_arg_invalid(runner):
  result = runner.invoke(cli, ['-i'])
  assert result.exit_code == 2
  assert result.output == jtv_help


def test_json_invalid(runner):
  result = runner.invoke(cli, ['-j'], input=invalid_json)
  assert result.exit_code == 0
  assert result.output == jtv_invalid_json


def test_yaml_invalid(runner):
  result = runner.invoke(cli, ['-y'], input=invalid_yaml)
  assert result.exit_code == 0
  assert result.output == jtv_invalid_yaml


def test_yaml_valid(runner):
  result = runner.invoke(cli, ['-y'], input=valid_yaml)
  assert result.exit_code == 0
  assert result.output == jtv_valid_yaml


def test_mode_invalid(runner):
  result = runner.invoke(cli, ['--mode', 'invaild-mode'], input=inconsistent_list_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_help


def test_object_empty_root_node(runner):
  result = runner.invoke(cli, ['-j'], input=object_empty_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_object_empty_root_node


def test_object_empty_nested_node(runner):
  result = runner.invoke(cli, ['-j'], input=object_empty_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_object_empty_nested_node


def test_list_empty_root_node(runner):
  result = runner.invoke(cli, ['-j'], input=list_empty_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_list_empty_root_node


def test_list_empty_nested_node(runner):
  result = runner.invoke(cli, ['-j'], input=list_empty_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_list_empty_nested_node


def test_string_empty_node(runner):
  result = runner.invoke(cli, ['-j'], input=string_empty_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_string_empty_node


def test_object_nested_node(runner):
  result = runner.invoke(cli, ['-j'], input=object_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_object_nested_node


def test_object_node_and_types(runner):
  result = runner.invoke(cli, ['-j'], input=object_node_and_types_json)
  assert result.exit_code == 0
  assert result.output == jtv_object_node_and_types


def test_mode_not_specified_for_consistent_list_root_node(runner):
  result = runner.invoke(cli, ['-j'], input=consistent_list_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_distinct_for_consistent_root_node


def test_mode_distinct_for_consistent_list_root_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'distinct'], input=consistent_list_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_distinct_for_consistent_root_node


def test_mode_first_for_consistent_list_root_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'first'], input=consistent_list_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_first_for_consistent_root_node


def test_mode_union_for_consistent_list_root_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'union'], input=consistent_list_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_union_for_consistent_root_node


def test_mode_not_specified_for_consistent_list_nested_node(runner):
  result = runner.invoke(cli, ['-j'], input=consistent_list_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_distinct_for_consistent_nested_node


def test_mode_distinct_for_consistent_list_nested_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'distinct'], input=consistent_list_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_distinct_for_consistent_nested_node


def test_mode_first_for_consistent_list_nested_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'first'], input=consistent_list_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_first_for_consistent_nested_node


def test_mode_union_for_consistent_list_nested_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'union'], input=consistent_list_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_union_for_consistent_nested_node


def test_mode_not_specified_for_inconsistent_list_root_node(runner):
  result = runner.invoke(cli, ['-j'], input=inconsistent_list_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_distinct_for_inconsistent_root_node


def test_mode_distinct_for_inconsistent_list_root_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'distinct'], input=inconsistent_list_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_distinct_for_inconsistent_root_node


def test_mode_first_for_inconsistent_list_root_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'first'], input=inconsistent_list_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_first_for_inconsistent_root_node


def test_mode_union_for_inconsistent_list_root_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'union'], input=inconsistent_list_root_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_union_for_inconsistent_root_node


def test_mode_not_specified_for_inconsistent_nested_list_node(runner):
  result = runner.invoke(cli, ['-j'], input=inconsistent_list_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_distinct_for_inconsistent_nested_node


def test_mode_distinct_for_inconsistent_nested_list_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'distinct'], input=inconsistent_list_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_distinct_for_inconsistent_nested_node


def test_mode_first_for_inconsistent_nested_list_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'first'], input=inconsistent_list_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_first_for_inconsistent_nested_node


def test_mode_union_for_inconsistent_nested_list_node(runner):
  result = runner.invoke(cli, ['-j', '--mode', 'union'], input=inconsistent_list_nested_node_json)
  assert result.exit_code == 0
  assert result.output == jtv_mode_union_for_inconsistent_nested_node
