# ===
# This is the main GYP file, which builds better-sqlite3 with SQLite3 itself.
# ===

{
  'includes': ['deps/common.gypi'],
  'variables': {
    'path_static_libcrypto': '<(module_root_dir)/openssl/1.1.1c/<(OS)_<(target_arch)/lib/libcrypto.a',
  },
  'targets': [
    {
      'target_name': 'better_sqlite3',
      'dependencies': ['deps/sqlite3.gyp:sqlite3'],
      'libraries': [
        '<(path_static_libcrypto)',
      ],
      'sources': ['src/better_sqlite3.cpp'],
      'cflags': [
        '-std=c++11',
      ],
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': [
          '-std=c++11',
          '-stdlib=libc++',
        ],
      },
    },
    {
      'target_name': 'test_extension',
      'dependencies': ['deps/sqlite3.gyp:sqlite3'],
      'conditions': [['sqlite3 == ""', { 'sources': ['deps/test_extension.c'] }]],
    },
    {
      'target_name': 'place_resulting_binaries',
      'type': 'none',
      'dependencies': ['better_sqlite3', 'test_extension'],
      'copies': [{
        'files': ['<(PRODUCT_DIR)/better_sqlite3.node', '<(PRODUCT_DIR)/test_extension.node', '<(path_static_libcrypto)'],
        'destination': 'build',
      }],
    },
  ],
}
