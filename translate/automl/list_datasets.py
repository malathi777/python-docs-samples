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


def list_datasets(project_id):
    """List datasets."""
    # [START automl_translate_list_dataset]
    from google.cloud import automl

    # TODO(developer): Uncomment and set the following variables
    # project_id = 'YOUR_PROJECT_ID'

    client = automl.AutoMlClient()
    # A resource that represents Google Cloud Platform location.
    project_location = client.location_path(project_id, 'us-central1')

    # List all the datasets available in the region.
    response = client.list_datasets(
        project_location, 'translation_dataset_metadata:*')

    print("List of datasets:")
    for dataset in response:
        print('Dataset name: {}'.format(dataset.name))
        print('Dataset id: {}'.format(dataset.name.split('/')[-1]))
        print('Dataset display name: {}'.format(dataset.display_name))
        print('Translation dataset metadata:')
        print(
            '\tsource_language_code: {}'.format(
                dataset.translation_dataset_metadata.source_language_code
            )
        )
        print(
            '\ttarget_language_code: {}'.format(
                dataset.translation_dataset_metadata.target_language_code
            )
        )
        print('Dataset create time:')
        print('\tseconds: {}'.format(dataset.create_time.seconds))
        print('\tnanos: {}'.format(dataset.create_time.nanos))
    # [END automl_translate_list_dataset]