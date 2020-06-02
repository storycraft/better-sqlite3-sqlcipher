# ===
# This is the main GYP file, which builds better-sqlite3 with SQLite3 itself.
# ===

{
  'includes': ['deps/common.gypi'],
  'conditions': [
    ['OS == "win"', {
      'variables': {
        'path_static_libcrypto': '<(module_root_dir)/openssl/1.0.2s/<(OS)_<(target_arch)/lib/libcrypto.dll.a',
      }
    },{
      'variables': {
        'path_static_libcrypto': '<(module_root_dir)/openssl/1.0.2s/<(OS)_<(target_arch)/lib/libcrypto.a',
      }
    }],
  ],
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
      'target_name': 'place_resulting_binaries',
      'type': 'none',
      'dependencies': ['better_sqlite3'],
      'conditions': [
        ['OS == "win"', {
          'copies': [{
            'files': [
              '<(module_root_dir)/openssl/1.0.2s/<(OS)_<(target_arch)/bin/libeay32.dll'
            ],
            'destination': 'build',
          }],
          'conditions': [
            ['target_arch == "ia32"', {
              'copies': [{
                'files': [
                  '<(module_root_dir)/dll/libgcc_s_dw2-1.dll'
                ],
                'destination': 'build',
              }],
            }],
          ]
        }]
      ],
      'copies': [{
        'files': [
          '<(PRODUCT_DIR)/better_sqlite3.node',
          '<(path_static_libcrypto)',
        ],
        'destination': 'build',
      }],
    },
  ],
}
