from typing import Any
from ortei import IORTEngine

class ExampleEngine(IORTEngine):
    def __init__(self):
        super().__init__()

    def _init_members(self, 
                      io_shape = {
                          "fake_input_image" : [1,3,1080,1920],
                          "fake_output_image" : [1,3,1080,1920],
                      }
                      ):

        self.ort_session = "fake_ort_session"
        self.io_shape = io_shape
        self.io_binding = "fake_in_binding"
        self.io_data_cpu = {key:"fake_data" for key in self.io_shape}
        self.io_data_ort = {key:"fake_data" for key in self.io_shape}
        self.device_name = "fake_device_name"
        self.input_data = "fake_input_data"
        self.output_data = "fake_output_data"

    def _bind_model_io(self) -> None:
        io_binding = self.io_binding
        io_data_ort = self.io_data_ort

        # do some binding
        # [example]
        # io_binding.bind_ortvalue_input("input_images", io_data_ort["input_images"])
        # io_binding.bind_ortvalue_output("output_images", io_data_ort["output_images"])

    def get_output_data(self) -> Any:
        return self.output_data

    def set_input_data(self, data: Any) -> None:
        self.input_data = data

    def convert_data2input(self) -> None:
        io_data_cpu = self.io_data_cpu
        input_data = self.input_data

        # do some converting
        # [example]
        # for c in range(3):
        #     io_data_cpu['input_images'][:,c,:,:] = input_data[:,:,:,c]

    def move_host2device(self) -> None:
        io_data_cpu = self.io_data_cpu
        io_data_ort = self.io_data_ort

        # do some converting
        # [example]
        # io_data_ort["input_images"].update_inplace(io_data_cpu["input_images"])
    
    def inference(self):
        ort_session = self.ort_session
        io_binding = self.io_binding

        # do some converting
        # [example]
        # ort_session.run_with_iobinding(io_binding)

    def move_device2host(self):
        io_data_ort = self.io_data_ort
        io_data_cpu = self.io_data_cpu

        # do some converting
        # [example]
        # io_data_cpu["output_images"][:] = io_data_ort["output_images"].numpy()[:]

    def convert_output2data(self):
        io_data_cpu = self.io_data_cpu
        result_images = self.output_data

        # do some converting
        # [example]
        # output = np.clip(np.multiply(io_data_cpu['output_images'], 255.), 0, 255)
        # for c in range(3):
        #     result_images[:,:,:,c] = output[:,c,:,:]