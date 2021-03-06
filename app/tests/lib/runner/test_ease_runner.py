import unittest

from app.lib.runner.runner import EaseRunner, RunnerException


argv = ['any', '/tmp']
argv_other = ['other', '/opt/ease']


class TestEaseRunner(unittest.TestCase):

    def setUp(self):
        # Hack, override config_dir to test make sense
        # Why? Because in other tests config_dir variable is set, a
        EaseRunner.get_instance().config_dir = argv[1]

    def test_should_correctly_instantiate_singleton_class_get_instance_should_always_get_same_result(self):
        instance = EaseRunner.get_instance(argv)
        instance_b = EaseRunner.get_instance()

        self.assertEqual(argv[1], instance.config_dir)
        self.assertEqual(instance, instance_b)

    def test_should_cannot_instantiate_second_instance_of_singleton_EasyRunner_class(self):
        EaseRunner.get_instance(argv)

        with self.assertRaises(RunnerException):
            EaseRunner(argv)

    def test_configuration_path_cannot_change_when_we_pass_argument_to_get_instance_method(self):
        EaseRunner.get_instance(argv)
        EaseRunner.get_instance(argv_other)
        instance = EaseRunner.get_instance()

        self.assertEqual(argv[1], instance.config_dir)
        self.assertNotEqual(argv_other[1], instance.config_dir)

    def test_runner_should_be_instantiated_with_empty_pipeline_list(self):
        instance = EaseRunner.get_instance(argv)

        self.assertIsNotNone(instance.pipeline_executors)
        self.assertEqual(0, len(instance.pipeline_executors))
