import pytest
import logging
from GenResClient import GenResClient
import Models as Ms
import os


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call':
        setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='function', autouse=False)
def client(request):
    session = GenResClient(os.environ['BASE_URL'])
    logging.info(f"Access token : {session.auth['Authorization']}")
    session.group = Ms.GroupOfModelStatic
    logging.info(f"Group Model : {session.group.__dict__}")
    yield session
    if request.node.rep_call.failed:
        for model in session.group.MODEL.__dict__.values():
            session.post_gql_request(query="""mutation delete($id: UUID!) {
          deleteModel(id: $id) 
        }""", variables={
                "id": f"{model.id}"
            })
