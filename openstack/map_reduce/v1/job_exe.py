# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack import resource2 as resource
from openstack import utils
from openstack.auto_scaling import auto_scaling_service
from openstack.auto_scaling.v1 import get_next_marker
from openstack.map_reduce import map_reduce_service


class JobExe(resource.Resource):
    """Map Reduce Job Exe Resource

    JobExe is not the same as :class: `~openstack.map_reduce.v1.job_execution.
    JobExecution`, It's an older version of job execution, we just implement
    it for backward compatible
    """
    resource_key = "job_execution"
    resources_key = "job_executions"
    base_path = "/job-exes"
    query_marker_key = "current_page"
    query_limit_key = "page_size"
    service = map_reduce_service.MapReduceService()

    # capabilities
    allow_list = True
    allow_get = True
    allow_delete = True

    _query_mapping = resource.QueryParameters(
        "id", "cluster_id", "job_name", "state", "page_size", "current_page"
    )

    #: Properties
    #: A dict contains job running information returned by Oozie
    info = resource.Body("info", type=dict)
    #: The cluster which executed the job
    cluster_id = resource.Body("cluster_id")
    #: The job id reference been executed
    job_id = resource.Body("job_id")
    #: The job name reference been executed
    job_name = resource.Body("job_name")
    #: The job type to be executed, valid values include:
    #: - 1: MapReduce
    #: - 2: Spark
    #: - 3: Hive Script
    #: - 4: HiveQL
    #: - 5: DistCp
    #: - 6: Spark Script
    #: - 7: Spark SQL
    job_type = resource.Body("job_type")
    #: Input data URL of the job execution
    input = resource.Body("input")
    #: Output data URL of the job execution
    output = resource.Body("output")
    #: The job execution group id
    group_id = resource.Body("group_id")
    #: The job execution group id
    jar_path = resource.Body("jar_path")
    #: The job log path
    job_log = resource.Body("job_log")
    #: File action: ``import`` , ``export`` ?
    file_action = resource.Body("file_action")
    #: Key parameter for program execution. The parameter is specified by the
    #: function of the user's internal program. MRS is only responsible for
    #: loading the parameter. This parameter can be empty.
    arguments = resource.Body("arguments")
    #: HiveQL statement
    hql = resource.Body("hql")
    #: Job status code, valid values include:
    #: - -1: Terminated
    #: - 1: Starting
    #: - 2: Running
    #: - 3: Completed
    #: - 4: Abnormal
    #: - 5: Error
    job_state = resource.Body("job_state")
    #: Job final status, valid values include:
    #: - 0: unfinished
    #: - 1: terminated due to an execution error
    #: - 2: executed successfully
    #: - 3: canceled
    job_final_status = resource.Body("job_final_status")
    #: Address of the Hive script
    hive_script_path = resource.Body("hive_script_path")
    #: User ID for creating jobs
    create_by = resource.Body("create_by")
    #: User ID for updating jobs
    update_by = resource.Body("update_by")
    #: Number of completed steps
    finished_step = resource.Body("finished_step")
    #: Main ID of a job
    job_main_id = resource.Body("job_main_id")
    #: Step ID of a job
    job_step_id = resource.Body("job_step_id")
    #: 	Delay time, which is a 13-bit timestamp.
    postpone_at = resource.Body("postpone_at")
    #: Step name of a job
    step_name = resource.Body("step_name")
    #: Number of steps
    step_num = resource.Body("step_num")
    #: Number of tasks
    task_num = resource.Body("task_num")
    #: Duration of job execution (unit: s)
    spend_time = resource.Body("spend_time")
    #: Step sequence of a job
    step_seq = resource.Body("step_seq")
    #: Job execution progress
    progress = resource.Body("progress")
    #: UTC date and time of the job-execution start time
    start_time = resource.Body("start_time")
    #: UTC date and time of the job-execution end time
    end_time = resource.Body("end_time")
    #: UTC date and time of the job-execution created time
    create_at = resource.Body("create_at")
    #: UTC date and time of the job-execution last updated time
    update_at = resource.Body("update_at")
    #: The tenant this job-execution belongs to
    tenant_id = resource.Body("tenant_id")

    @classmethod
    def get_next_marker(cls, response_json, yielded, query_params):
        page_size = query_params.get("page_size", 1)
        if yielded < page_size:
            return -1

        current_page = int(query_params.get("current_page", 1))
        return current_page + 1
