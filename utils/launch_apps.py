import os
import sys
import time
sys.path.insert(1, '..')

import argparse

APPLICATIONS = ['hello_world', 'book_info', 'online_boutique', 'hotel_reservation', 'sock_shop', 'train_ticket']
SUFFIXES = {
            'online_boutique': ':80', 
            'book_info': '/productpage', 
            'hello_world': ':80/hello', 
            'hotel_reservation': ':80', 
            'sock_shop':':80',
            'train_ticket': ':80',
           }

def launch_application(app_name='online_boutique', delete_existing_apps=True, other_applications=['helloworld', 'bookinfo', 'online_boutique', 'hotel_reservation', 'sock_shop', 'trainticket', 'synthlarge']):
    """
    Launch the specified microservice application.
    Requires cloud provider authentication to already be configured.

    Args:
        app_name (str, optional): Name of the application. Defaults to 'online_boutique'.

    Returns:
        _type_: Landing page URL for the application.
    """
    
    # Stop all applications
    if delete_existing_apps is True:
        for application in APPLICATIONS:
            os.system('kubectl delete -f microservices/{}/deployments.yaml'.format(application))
            os.system('kubectl delete -f microservices/{}/gateway.yaml'.format(application))


    # Launch specified application
    os.system('kubectl apply -f microservices/{}/deployments.yaml'.format(app_name))
    os.system('kubectl apply -f microservices/{}/gateway.yaml'.format(app_name))


    # Get host of the application and return.
    time.sleep(30) # Wait for the app and gateway to come up.
    ingress_host = os.popen("kubectl -n default get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}'").read()

    # Create users for train ticket application.
    if app_name == 'trainticket':
        time.sleep(60)
        os.system('locust -f load_generator/locustfiles/trainticket/create_users.py --headless -u 100 -r 10 --host http://{ingress_host} --run-time 240s'.format(ingress_host=ingress_host))
        os.system('locust -f load_generator/locustfiles/trainticket/create_users.py --headless -u 100 -r 10 --host http://{ingress_host} --run-time 240s'.format(ingress_host=ingress_host))

    print("Host = {ingress_host}".format(ingress_host=ingress_host+SUFFIXES[app_name]))
    return

def delete_applications():
    """
    Deletes the deployment and gateway for all applications.
    """

    # Stop all applications
    for application in APPLICATIONS:
        os.system('kubectl delete -f microservices/{}/deployments.yaml'.format(application))
        os.system('kubectl delete -f microservices/{}/gateway.yaml'.format(application))

    return

def get_host(app_name):
    """
    Get the host URL for an application.

    Args:
        app_name (str): Name of application

    Returns:
        str: host URL
    """
    ingress_host = os.popen("kubectl -n default get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}'").read()
    return ingress_host+SUFFIXES[app_name]

if __name__ == "__main__":

    delete_applications()

    # Parse application from command line.
    parser = argparse.ArgumentParser()
    parser.add_argument('application', type=str, default='online_boutique')
    args = parser.parse_args()
    print(args)
    app_name = args.application

    # Launch application.
    host = launch_application(app_name)
    print(host)
