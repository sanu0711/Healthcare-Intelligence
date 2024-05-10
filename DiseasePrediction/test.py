import markdown

text="**Amethi District Hospital**\n\n* Address: Dewa Road, Amethi, Uttar Pradesh 227401\n* Phone: 05354-222378\n* Website: http://health.up.nic.in/amethi\n\n**Facilities:**\n\n* General medicine\n* Surgery\n* Gynecology and obstetrics\n* Pediatrics\n* Ophthalmology\n* Ear, nose, and throat (ENT)\n* Radiology and imaging\n* Laboratory services\n* Emergency care\n\n**Sanjay Gandhi Institute of Trauma & Orthopaedics (SGITO)**\n\n* Address: Lucknow-Sultanpur Road, Mohanlalganj, Uttar Pradesh 226401\n* Phone: 0522-2770021\n* Website: http://sgitotrauma.com/\n\n**Facilities:**\n\n* Orthopedics and traumatology\n* General surgery\n* Plastic surgery\n* Neurosurgery\n* Rehabilitation medicine\n* Radiology and imaging\n* Laboratory services\n\n**Note:** SGITO is located approximately 60 km from RGIPT Jais."

fit = markdown.markdown(text)
print(fit)


