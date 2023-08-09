import unittest
import os
from example_engine import ExampleEngine
from ortei import EngineEvaluator

# TestCase를 작성
class EngineTests(unittest.TestCase):

    def setUp(self):
        """테스트 시작되기 전 파일 작성"""
        self.engin = ExampleEngine()

    def tearDown(self):
        """테스트 종료 후 파일 삭제 """
        try:
            pass
        except:
            pass

    def test_set_input_data(self):
        self.engin.set_input_data("fake_input")

    def test_convert_data2input(self):
        self.engin.convert_data2input()

    def test_move_host2device(self):
        self.engin.move_host2device()

    def test_inference(self):
        self.engin.inference()

    def test_move_device2host(self):
        self.engin.move_device2host()

    def test_convert_output2data(self):
        self.engin.convert_output2data()

    def test_get_output_data(self):
        self.engin.get_output_data()

class EvaluatorTests(unittest.TestCase):

    def setUp(self):
        """테스트 시작되기 전 파일 작성"""
        self.engin = ExampleEngine()
        self.dataset = [i for i in range(100)]
        self.evaluator = EngineEvaluator(self.engin)
        self.test_result_path = f"./temp_test_run_and_save_result.csv"

    def tearDown(self):
        """테스트 종료 후 파일 삭제 """
        csv_path = self.test_result_path
        try:
            os.remove(csv_path)
            assert not os.path.exists(csv_path)
        except Exception as ex:
            print(ex)
    
    def test_run_and_save(self):
        test_result_path = self.test_result_path
        evaluator = self.evaluator
        dataset = self.dataset

        evaluator.run(dataset)
        evaluator.save_testdata(test_result_path)
        assert os.path.exists(test_result_path)
        os.system(f"cat {test_result_path}")

# unittest를 실행
if __name__ == '__main__':
    unittest.main()