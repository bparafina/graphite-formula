def test_graphite_is_listening(Socket):
    socket = Socket("tcp://0.0.0.0:8000")
    assert socket.is_listening


def test_graphite_service_is_running(Service):
    service = Service("graphite")
    assert service.is_running
    assert service.is_enabled
