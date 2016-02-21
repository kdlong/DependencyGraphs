# coding: utf-8
import re
myfile = open("test.txt", "r")
text = myfile.readlines()
parsed = re.findall("'.*?'", ''.join(text))

module_dict = {i[0].strip("'") : i[1].strip("'") for i in zip(parsed[0::3], parsed[1::3])}

object_dict = {x : [] for x in module_dict.values()}
for module, phys_obj in module_dict.iteritems():
    object_dict[phys_obj].append(module)

header = []
body = []
i = 0
j = 0
for phys_obj, modules in object_dict.iteritems():
    object_name = 'module%i' % i
    header.append('%s [label="%s"]' % (object_name, phys_obj))
    i += 1
    for module in modules:
        j += 1
        module_name = 'object%i' % j 
        header.append('%s [label="%s"]' % (module_name, module.replace("::", "\::")))
        body.append("%s -> %s" % (module_name, object_name))
with open("graphtest.gv", "w") as graph_file:
    graph_file.write("digraph GraphTest {\n\t")
    graph_file.write("\n\t".join(header + ["\n"] + body))
    graph_file.write("\n}")
    
