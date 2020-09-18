from fileinfo.fileinfo import FileInfo
from unittest.mock import patch


def test_init():
    filename = 'somefile.ext'
    fi = FileInfo(filename)
    assert fi.filename == filename

def test_init_relative():
    filename = 'somefile.ext'
    relative_path = '../{}'.format(filename)
    fi = FileInfo(relative_path)
    assert fi.filename == filename

@patch('os.path.getsize')
@patch('os.path.abspath')
def test_get_info(abspath_mock, getsize_mock):
    test_abspath = 'some/abs/path'
    abspath_mock.return_value = test_abspath
    
    filename = 'somefile.ext'
    original_path = '../{}'.format(filename)

    test_size = 1234
    getsize_mock.return_value = test_size
        
    f1 = FileInfo(original_path)
    assert f1.get_info() == (filename, original_path, test_abspath, test_size)