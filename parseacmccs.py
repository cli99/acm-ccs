import skos
import rdflib
import os
import json

def getbroaderconcept(filename,conceptid):
	graph = rdflib.Graph()
	graph.load(filename)
	loader = skos.RDFLoader(graph)
	# concept = loader["file://" + os.path.abspath(filename) + "#" + str(conceptid)]
	# a = concept.broader.items()[0][1]
	# print a.prefLabel.decode().title()

	o = loader.keys()

	f = open('out.txt', 'w')
	# for ii in o:
	# 	print >> f, ii
	print(graph)

	return 1

filename  = "ACMComputingClassificationSystemSKOSTaxonomy.xml"
getbroaderconcept("ACMComputingClassificationSystemSKOSTaxonomy.xml",10011182 )