# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.18

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CMake.app/Contents/bin/cmake

# The command to remove a file.
RM = /Applications/CMake.app/Contents/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/ryanmclean/Desktop/4150/image-blurring

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/ryanmclean/Desktop/4150/image-blurring

# Include any dependencies generated for this target.
include CMakeFiles/blur-image.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/blur-image.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/blur-image.dir/flags.make

CMakeFiles/blur-image.dir/blur-image.cpp.o: CMakeFiles/blur-image.dir/flags.make
CMakeFiles/blur-image.dir/blur-image.cpp.o: blur-image.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/ryanmclean/Desktop/4150/image-blurring/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/blur-image.dir/blur-image.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/blur-image.dir/blur-image.cpp.o -c /Users/ryanmclean/Desktop/4150/image-blurring/blur-image.cpp

CMakeFiles/blur-image.dir/blur-image.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/blur-image.dir/blur-image.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/ryanmclean/Desktop/4150/image-blurring/blur-image.cpp > CMakeFiles/blur-image.dir/blur-image.cpp.i

CMakeFiles/blur-image.dir/blur-image.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/blur-image.dir/blur-image.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/ryanmclean/Desktop/4150/image-blurring/blur-image.cpp -o CMakeFiles/blur-image.dir/blur-image.cpp.s

# Object files for target blur-image
blur__image_OBJECTS = \
"CMakeFiles/blur-image.dir/blur-image.cpp.o"

# External object files for target blur-image
blur__image_EXTERNAL_OBJECTS =

blur-image: CMakeFiles/blur-image.dir/blur-image.cpp.o
blur-image: CMakeFiles/blur-image.dir/build.make
blur-image: /usr/local/lib/libopencv_gapi.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_stitching.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_alphamat.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_aruco.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_bgsegm.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_bioinspired.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_ccalib.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_dnn_objdetect.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_dnn_superres.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_dpm.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_face.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_freetype.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_fuzzy.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_hfs.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_img_hash.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_intensity_transform.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_line_descriptor.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_quality.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_rapid.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_reg.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_rgbd.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_saliency.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_sfm.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_stereo.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_structured_light.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_superres.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_surface_matching.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_tracking.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_videostab.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_viz.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_xfeatures2d.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_xobjdetect.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_xphoto.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_highgui.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_shape.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_datasets.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_plot.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_text.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_dnn.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_ml.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_phase_unwrapping.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_optflow.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_ximgproc.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_video.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_videoio.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_imgcodecs.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_objdetect.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_calib3d.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_features2d.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_flann.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_photo.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_imgproc.4.4.0.dylib
blur-image: /usr/local/lib/libopencv_core.4.4.0.dylib
blur-image: CMakeFiles/blur-image.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/ryanmclean/Desktop/4150/image-blurring/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable blur-image"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/blur-image.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/blur-image.dir/build: blur-image

.PHONY : CMakeFiles/blur-image.dir/build

CMakeFiles/blur-image.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/blur-image.dir/cmake_clean.cmake
.PHONY : CMakeFiles/blur-image.dir/clean

CMakeFiles/blur-image.dir/depend:
	cd /Users/ryanmclean/Desktop/4150/image-blurring && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/ryanmclean/Desktop/4150/image-blurring /Users/ryanmclean/Desktop/4150/image-blurring /Users/ryanmclean/Desktop/4150/image-blurring /Users/ryanmclean/Desktop/4150/image-blurring /Users/ryanmclean/Desktop/4150/image-blurring/CMakeFiles/blur-image.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/blur-image.dir/depend

