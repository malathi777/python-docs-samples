#!/usr/bin/env python

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def get_model_evaluation(project_id, model_id, model_evaluation_id):
    """Get model evaluation."""
    # [START automl_translate_get_model_evaluation]
    from google.cloud import automl

    # TODO(developer): Uncomment and saet the following variables
    # project_id = 'YOUR_PROJECT_ID'
    # model_id = 'YOUR_MODEL_ID'
    # model_evaluation_id = 'YOUR_MODEL_EVALUATION_ID'

    client = automl.AutoMlClient()
    # Get the full path of the model evaluation.
    model_evaluation_full_id = client.model_evaluation_path(
        project_id, 'us-central1', model_id, model_evaluation_id
    )

    # Get complete detail of the model evaluation.
    response = client.get_model_evaluation(model_evaluation_full_id)

    print('Model evaluation name: {}'.format(response.name))
    print('Model annotation spec id: {}'.format(response.annotation_spec_id))
    print('Create Time:')
    print('\tseconds: {}'.format(response.create_time.seconds))
    print('\tnanos: {}'.format(response.create_time.nanos / 1e9))
    print('Evaluation example count: {}'.format(
        response.evaluated_example_count))
    print('Model evaluation metrics: {}'.format(
        response.translation_evaluation_metrics))
    # [END automl_translate_get_model_evaluation]