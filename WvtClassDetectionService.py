# Copyright 2020 gRPC authors.
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
"""The Python AsyncIO implementation of the GRPC helloworld.Greeter server."""

import logging
import asyncio
import grpc

import RegionProposed_pb2_grpc
import RegionProposed_pb2

print("Hello World! Welcome to Python Examples.")

class RegionProposalService(RegionProposed_pb2_grpc.RegionProposed):

    async def ProcessMp4File(
            self, request: RegionProposed_pb2_grpc.RegionProposed,
            context: grpc.aio.ServicerContext) -> RegionProposed_pb2.InputFileMp4:
        logging.info("started processing")

        print("started processing")
        yield RegionProposed_pb2.DetectionFrame(FrameNumber=5)


    async def TestMet(
            self, request: RegionProposed_pb2_grpc.RegionProposed,
            context: grpc.aio.ServicerContext) -> RegionProposed_pb2.testInput:
        logging.info("started processing")

        print("started processing")
        return RegionProposed_pb2.TestOutput(xyz='message 1')


async def serve() -> None:
    server = grpc.aio.server()
    RegionProposed_pb2_grpc.add_RegionProposedServicer_to_server(RegionProposalService(), server)
    listen_addr = '[::]:50058'
    server.add_insecure_port(listen_addr)
    print("Starting server on %s", listen_addr)
    await server.start()
    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        # Shuts down the server with 0 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(0)


if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO)
    #asyncio.run(serve())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(serve())