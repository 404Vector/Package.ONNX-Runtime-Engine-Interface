# Package.ONNX-Runtime-Engine-Interface

ONNX Runtime으로 Engine을 만들 때 공통으로 사용할 수 있는 Interface를 제공합니다.

## Status

[![Basic PR Check](https://github.com/404Vector/Package.ONNX-Runtime-Engine-Interface/actions/workflows/workflow_pr_check_basic.yml/badge.svg?branch=main)](https://github.com/404Vector/Package.ONNX-Runtime-Engine-Interface/actions/workflows/workflow_pr_check_basic.yml)  

[![Publish Python distributions to PyPI](https://github.com/404Vector/Package.ONNX-Runtime-Engine-Interface/actions/workflows/workflow_publish_pypi.yml/badge.svg?branch=main)](https://github.com/404Vector/Package.ONNX-Runtime-Engine-Interface/actions/workflows/workflow_publish_pypi.yml)  
 -> [pypi package link](https://pypi.org/project/ortei/)

## Evaluation

IORTEngine을 상속한 class는 EngineEvaluator를 사용하여 각 요소의 시간을 측정할 수 있습니다.

측정된 결과는 json으로 저장할 수 있으며 [ORTEI-Viewer 프로젝트](https://github.com/404Vector/App.ORTEI-Viewer)를 통해 시각화할 수 있습니다.
