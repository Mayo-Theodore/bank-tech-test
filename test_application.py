# from pathlib import Path


# def getssh():
#     """Simple function to return expanded homedir ssh path."""
#     return Path.home() / ".ssh"


# def test_getssh(monkeypatch):
#     # mocked return function to replace Path.home
#     # always return '/abc'
#     def mockreturn():
#         return Path("/abc")

#     # Application of the monkeypatch to replace Path.home
#     # with the behavior of mockreturn defined above.
#     monkeypatch.setattr(Path, "home", mockreturn)

#     # Calling getssh() will use mockreturn in place of Path.home
#     # for this test with the monkeypatch.
#     x = getssh()
#     assert x == Path("/abc/.ssh")





# # def test_get_current_directory(monkeypatch):
# #     """
# #     GIVEN a monkeypatched version of os.getcwd()
# #     WHEN example1() is called
# #     THEN check the current directory returned
# #     """
# #     def mock_getcwd():
# #         return '/data/user/directory123'

# #     monkeypatch.setattr(os, 'getcwd', mock_getcwd)
# #     assert example1() == '/data/user/directory123'