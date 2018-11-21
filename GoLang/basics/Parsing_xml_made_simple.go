package main

import (
	"encoding/xml"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main(){
	/*https://www.washingtonpost.com/news-business-sitemap.xml */
	resp, _ := http.Get("https://www.washingtonpost.com/news-business-sitemap.xml")
	bytes, _ := ioutil.ReadAll(resp.Body)
	resp.Body.Close()

	var s SiteMapIndexX
	xml.Unmarshal(bytes,&s)

	for index, url := range s.Locations {
		fmt.Println(index, url)
	}
}

type SiteMapIndexX struct {
	Locations []string `xml:"url>loc"` //value of loc tag inside url tag
}

