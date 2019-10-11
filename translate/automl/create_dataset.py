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


def create_dataset(project_id, display_name):
    """Create a dataset."""
    # [START automl_translate_create_dataset]
    from google.cloud import automl

    # TODO(developer): Uncomment and set the following variables
    # project_id = 'YOUR_PROJECT_ID'
    # display_name = 'YOUR_DATASET_NAME'

    client = automl.AutoMlClient()

    # A resource that represents Google Cloud Platform location.
    project_location = client.location_path(project_id, 'us-central1')
    dataset_metadata = automl.types.TranslationDatasetMetadata(
        source_language_code='en',
        target_language_code='ja')
    dataset = automl.types.Dataset(
        display_name=display_name,
        translation_dataset_metadata=dataset_metadata)

    # Create a dataset with the dataset metadata in the region.
    response = client.create_dataset(project_location, dataset)

    created_dataset = response.result()

    # Display the dataset information
    print('Dataset name: {}'.format(created_dataset.name))
    print('Dataset id: {}'.format(created_dataset.name.split("/")[-1]))
    print('Dataset display name: {}'.format(created_dataset.display_name))
    print('Translation dataset Metadata:')
    print(
        '\tsource_language_code: {}'.format(
            created_dataset.translation_dataset_metadata.source_language_code
        )
    )
    print(
        '\ttarget_language_code: {}'.format(
            created_dataset.translation_dataset_metadata.target_language_code
        )
    )
    print('Dataset create time:')
    print('\tseconds: {}'.format(created_dataset.create_time.seconds))
    print('\tnanos: {}'.format(created_dataset.create_time.nanos))
    # [END automl_translate_create_dataset]