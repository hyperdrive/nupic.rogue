#!/usr/bin/env python
#------------------------------------------------------------------------------
# Copyright 2013-2014 Numenta Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------
from agent import AvogadroAgent
import psutil

from model_params import getModelParams



class AvogadroNetworkBytesSentAgent(AvogadroAgent):
  name = "NetworkBytesSent"
  datasourceType = "DERIVE"
  min = 0.0
  max = 1000000

  ENCODER_PARAMS = {
    name: {
      "clipInput": True,
      "fieldname": name,
      "maxval": max,
      "minval": min,
      "n": 50,
      "name": name,
      "type": "ScalarEncoder",
      "w": 21
    }
  }

  MODEL_PARAMS = getModelParams(ENCODER_PARAMS, name)

  def collect(self):
    return psutil.net_io_counters().bytes_sent



class AvogadroNetworkBytesReceivedAgent(AvogadroAgent):
  name = "NetworkBytesReceived"
  datasourceType = "DERIVE"
  min = 0.0
  max = 1000000

  ENCODER_PARAMS = {
    name: {
      "clipInput": True,
      "fieldname": name,
      "maxval": max,
      "minval": min,
      "n": 50,
      "name": name,
      "type": "ScalarEncoder",
      "w": 21
    }
  }

  MODEL_PARAMS = getModelParams(ENCODER_PARAMS, name)

  def collect(self):
    return psutil.net_io_counters().bytes_recv
