FROM nvidia/cuda:11.1-devel-ubuntu18.04

# OpenGL - (glvnd)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxau6 \
    libxdmcp6 \
    libxcb1  \
    libxext6 \
    libx11-6 \
    pkg-config \
    libglvnd-dev \
    libgl1-mesa-dev \
    libegl1-mesa-dev \
    libgles2-mesa-dev \
    mesa-utils \
    && rm -rf /var/lib/apt/lists/*
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics,compat32

# Pre-requsities, development tools and taichi requirements.
RUN apt-get update \
    && apt-get install -y software-properties-common \
    unzip wget git \
    build-essential gdb \
    libtinfo-dev clang-8 \
    python3-dev python3-pip \
    libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev zlib1g-dev

# Python packages
RUN apt-get update \
    && apt-get install -y python3-dev python3-pip

# Package clean up (reduce image size)
RUN apt-get autoremove -y \
    && apt-get clean -y

# Configure a SUDO non-root user (no password)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

# Install these packages in the context of user

# Generic python libraries
RUN python3 -m pip install autopep8

# Taichi
RUN python3 -m pip install taichi taichi_glsl taichi_three