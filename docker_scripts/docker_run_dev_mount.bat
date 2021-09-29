docker run --env-file .\command_line_env.env -p 5000:5000 --mount type=bind,source=C:\DevOps\DevOps-Course-Starter/todo_app,target=/my-work-dir/todo_app todo-app:dev
docker run -it --entrypoint /bin/bash my-test-image:latest -s
