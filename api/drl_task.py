def run_drl_task(request_handler, msg):
    print(msg)
    request_handler.wfile.write('run_drl_task()from req handler '.encode('utf-8'))
    # Add your DRL script logic here
