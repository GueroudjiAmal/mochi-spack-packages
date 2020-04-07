##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class HepnosDataloader(CMakePackage):
    """Dataloader for HEPnOS."""

    homepage = "https://xgitlab.cels.anl.gov/sds/hep/HEPnOS-Dataloader"
    url = "https://xgitlab.cels.anl.gov/sds/hep/HEPnOS-Dataloader"
    git = 'https://xgitlab.cels.anl.gov/sds/hep/HEPnOS-Dataloader.git'

    version('develop', branch='master')
    version('master', branch='master')
    version('0.2',   tag='v0.2')
    version('0.1',   tag='v0.1')

    depends_on('cmake@3.1.0:', type=('build'))
    depends_on('mpi')
    depends_on('hepnos@0.3.1:')
    depends_on('tclap')
    depends_on('spdlog')
    depends_on('hdf5')
    depends_on('boost+serialization')

    def cmake_args(self):
        extra_args = ['-DBUILD_SHARED_LIBS=ON']
        extra_args.extend(['-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx])
        return extra_args