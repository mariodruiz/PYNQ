#   Copyright (c) 2026, Advanced Micro Devices, Inc.
#   SPDX-License-Identifier: BSD-3-Clause

import warnings

warnings.warn(
    "pynq.lib.video.pcam5c is deprecated; use pynq.lib.video.mipi_camera",
    DeprecationWarning,
    stacklevel=2,
)

from .mipi_camera import MIPICamera as Pcam5C, MIPIMode
