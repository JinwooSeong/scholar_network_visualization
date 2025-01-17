import json

if __name__ == '__main__':
    topic_dict = {}
    topic_dict['graph-T16_sub0.net'] = "Data_Mining"
    topic_dict['graph-T107_sub1.net'] = "Web_Services"
    topic_dict['graph-T131_sub0.net'] = "Bayesian_Networks"
    topic_dict['graph-T144_sub4.net'] = "Web_Mining"
    topic_dict['graph-T145_sub0.net'] = "Semantic_Web"
    topic_dict['graph-T162_sub1.net'] = "Machine_Learning"
    topic_dict['graph-T24_sub0.net'] = "Database_Systems"
    topic_dict['graph-T75_sub0.net'] = "Information_Retrieval"
    size_dict = {}
    size_dict["Data_Mining"] = 679
    size_dict["Web_Services"] = 400
    size_dict["Bayesian_Networks"] = 554
    size_dict["Web_Mining"] = 348
    size_dict["Semantic_Web"] = 671
    size_dict["Machine_Learning"] = 976
    size_dict["Database_Systems"] = 1127
    size_dict["Information_Retrieval"] = 657

    for topic in topic_dict.values():
        field = []
        for time in range(1):
            obj = {}
            obj["time"] = "2020-03"
            obj["data"] = {}
            nodes = []
            links = []
            largestNodeSize = size_dict[topic]
            with open(topic+".json")as f:
                detail_data = json.load(f)
                authors = detail_data["author"]
                relations = detail_data["relation"]
            with open("person2id.json")as f:
                person2id = json.load(f)
            for author in authors:
                node = {}
                node["id"] = author[0]
                node["name"] = author[1]
                node["_size"] = author[2]
                if node["name"]in person2id:
                    node["link"] ="https://www.aminer.cn/profile/"+node["name"] + "/"+person2id[node["name"]]
                else:
                    node["link"] = "https://www.aminer.cn/profile/"+node["name"]
                node["info"] = {}
                node["info"]["paper"] = author[2]
                nodes.append(node)
            for relation in relations:
                link = {}
                link["id"] = relation[0]
                link["name"] = "coauthor"
                link["sid"] = relation[1]
                link["tid"] = relation[2]
                links.append(link)
            obj["data"]["nodes"] = list(reversed(nodes))
            obj["data"]["largestNodeSize"] = largestNodeSize
            obj["data"]["links"] = links

            field.append(obj)
        with open(topic+"_detail.json", "w")as f:
            f.write(json.dumps(field))

