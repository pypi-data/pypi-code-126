from producer import CallGraphGenerator
coord = { "product": "leanium",
          "version": "0.1a2",
          "version_timestamp": "2000",
          "requires_dist": []}
generator = CallGraphGenerator("directoryName", coord)
generator.generate()