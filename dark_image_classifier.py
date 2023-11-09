N = np.zeros((5040,1)
    import os.path
    for i in range(len(N)):
    	text = str(i)+'.jpg'
    	if os.path.exists(text):
   	    image = cv2.imread(text)
         else:
    	     continue
    	 img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    	 mea = np.mean(img)
    	 med = np.median(img)
    	 if med<75:
    	    if mea-med<20:
    	       N[i] = 1
    	 else:
    	    continue
