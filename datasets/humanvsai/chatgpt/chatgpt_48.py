def write_submission_script(**kwargs):
    exec_args = kwargs.get('exec_args', [])
    script_path = 'submission_script.sh'
    with open(script_path, 'w') as script:
        script.write('#!/bin/bash\n')
        script.write(f'task.executable {" ".join(exec_args)}\n')
    return script_path
