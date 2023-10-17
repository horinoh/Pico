
set(ProjectName "Hello")
add_executable(${ProjectName}
        main.c
        )

# pull in common dependencies
target_link_libraries(${ProjectName} pico_stdlib)

# create map/bin/hex/uf2 file etc.
pico_add_extra_outputs(${ProjectName})

# add url via pico_set_program_url
#example_auto_set_url(${ProjectName})
