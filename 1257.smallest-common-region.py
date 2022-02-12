class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        regionGraph = defaultdict()

        def buildGraph():
            for region in regions:
                parent = region[0]
                for area in region[1:]:
                    regionGraph[area] = parent

        buildGraph()
        parents = {}
        while region1:
            if regionGraph.get(region1, None):
                parents[region1] = regionGraph[region1]
            else:
                parents[region1] = region1
            region1 = regionGraph.get(region1, None)

        while region2:
            if region2 in parents:
                return region2
            elif regionGraph[region2] in parents:
                return regionGraph[region2]
            else:
                region2 = regionGraph[region2]

        return None
