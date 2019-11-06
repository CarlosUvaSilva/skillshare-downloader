from downloader import Downloader

cookie = """
device_session_id=*******
"""

dl = Downloader(cookie=cookie)

# download by class URL:
# dl.download_course_by_url('https://www.skillshare.com/classes/Art-Fundamentals-in-One-Hour/189505397')
# dl.download_course_by_url('https://www.skillshare.com/classes/Color-Grading-for-Filmmaking-The-Vision-Art-and-Science/163600258')
# or by class ID:
# dl.download_course_by_class_id(189505397)


dl_array = [
]


for v in dl_array:
  dl.download_course_by_url(v)
