import os

SF_MIRROR = 'http://iweb.dl.sourceforge.net'
PILLOW_DEPENDS_DIR = 'C:\\pillow-depends\\'

pythons = {  # '26': 7,
           '27': 7,
           # '32': 7,
           '33': 7.1,
           '34': 7.1}

VIRT_BASE = "c:/vp/"
X64_EXT = os.environ.get('X64_EXT', "x64")

libs = {
    # 'openjpeg': {
    #     'filename': 'openjpeg-2.0.0-win32-x86.zip',
    #     'hash': 'sha1:xxx',
    #     'version': '2.0'
    # },
    'zlib': {
        'url': 'http://zlib.net/zlib128.zip',
        'filename': PILLOW_DEPENDS_DIR + 'zlib128.zip',
        'hash': 'md5:126f8676442ffbd97884eb4d6f32afb4',
        'dir': 'zlib-1.2.8',
    },
    'jpeg': {
        'url': 'http://www.ijg.org/files/jpegsr9b.zip',
        'filename': PILLOW_DEPENDS_DIR + 'jpegsr9b.zip',
        'hash': 'md5:a21b8024d78ba05857a75272b4fa95ec',  # not found - generated by wiredfool
        'dir': 'jpeg-9b',
    },
    'tiff': {
        'url': 'ftp://ftp.remotesensing.org/pub/libtiff/tiff-4.0.6.zip',
        'filename': PILLOW_DEPENDS_DIR + 'tiff-4.0.6.zip',
        'hash': 'md5:f5b485d750b2001255ed64224b98b857',
        'dir': 'tiff-4.0.6',
    },
    'freetype': {
        'url': 'http://download.savannah.gnu.org/releases/freetype/freetype-2.7.tar.gz',
        'filename': PILLOW_DEPENDS_DIR + 'freetype-2.7.tar.gz',
        'hash': 'md5:337139e5c7c5bd645fe130608e0fa8b5',
        'dir': 'freetype-2.7',
    },
    'lcms': {
        'url': SF_MIRROR+'/project/lcms/lcms/2.7/lcms2-2.7.zip',
        'filename': PILLOW_DEPENDS_DIR + 'lcms2-2.7.zip',
        'hash': 'sha1:7ff1a5b721ca719760ba6eb4ec6f38d5e65381cf',
        'dir': 'lcms2-2.7',
    },
    'tcl-8.5': {
        'url': SF_MIRROR+'/project/tcl/Tcl/8.5.19/tcl8519-src.zip',
        'filename': PILLOW_DEPENDS_DIR + 'tcl8519-src.zip',
        'hash': 'sha1:9de57fd34bd688716c16c978db96fa16a5fde924',
        'dir': '',
    },
    'tk-8.5': {
        'url': SF_MIRROR+'/project/tcl/Tcl/8.5.19/tk8519-src.zip',
        'filename': PILLOW_DEPENDS_DIR + 'tk8519-src.zip',
        'hash': 'sha1:78d0d2c81e024e0b48bfd7b2cc16718f08f46ed9',
        'dir': '',
        'version': '8.5.19',
    },
    'tcl-8.6': {
        'url': SF_MIRROR+'/project/tcl/Tcl/8.6.6/tcl866-src.zip',
        'filename': PILLOW_DEPENDS_DIR + 'tcl866-src.zip',
        'hash': 'md5:45dae95abc12a5f8c29dca5baf169a13',
        'dir': '',
    },
    'tk-8.6': {
        'url': SF_MIRROR+'/project/tcl/Tcl/8.6.6/tk866-src.zip',
        'filename': PILLOW_DEPENDS_DIR + 'tk866-src.zip',
        'hash': 'md5:5004cc0ed2ab820406a36a0c0553b917',
        'dir': '',
        'version': '8.6.6',
    },
    'webp': {
        'url': 'http://downloads.webmproject.org/releases/webp/libwebp-0.5.2.tar.gz',
        'filename': PILLOW_DEPENDS_DIR + 'libwebp-0.5.2.tar.gz',
        'hash': 'sha1:c3adfa47f96a3909fb05e41636fdcbe3826edfbd',
        'dir': 'libwebp-0.5.2',
    },
    'openjpeg': {
        'url': SF_MIRROR+'/project/openjpeg/openjpeg/2.1.2/openjpeg-2.1.2.tar.gz',
        'filename': PILLOW_DEPENDS_DIR + 'openjpeg-2.1.2.tar.gz',
        'hash': 'md5:40a7bfdcc66280b3c1402a0eb1a27624',
        'dir': 'openjpeg-2.1.2',
    },
}

compilers = {
    (7, 64): {
        'env_version': 'v7.0',
        'vc_version': '2008',
        'env_flags': '/x64 /xp',
        'inc_dir': 'msvcr90-x64',
        'platform': 'x64',
        'webp_platform': 'x64',
    },
    (7, 32): {
        'env_version': 'v7.0',
        'vc_version': '2008',
        'env_flags': '/x86 /xp',
        'inc_dir': 'msvcr90-x32',
        'platform': 'Win32',
        'webp_platform': 'x86',
    },
    (7.1, 64): {
        'env_version': 'v7.1',
        'vc_version': '2010',
        'env_flags': '/x64 /vista',
        'inc_dir': 'msvcr10-x64',
        'platform': 'x64',
        'webp_platform': 'x64',
    },
    (7.1, 32): {
        'env_version': 'v7.1',
        'vc_version': '2010',
        'env_flags': '/x86 /vista',
        'inc_dir': 'msvcr10-x32',
        'platform': 'Win32',
        'webp_platform': 'x86',
    },
}


def pyversion_from_env():
    py = os.environ['PYTHON']

    py_version = '27'
    for k in pythons.keys():
        if k in py:
            py_version = k
            break

    if '64' in py:
        py_version = '%s%s' % (py_version, X64_EXT)

    return py_version


def compiler_from_env():
    py = os.environ['PYTHON']

    for k, v in pythons.items():
        if k in py:
            compiler_version = v
            break

    bit = 32
    if '64' in py:
        bit = 64

    return compilers[(compiler_version, bit)]