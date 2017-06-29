
# Russian DNS Leak (All .ru, .su, .tatar, .рф, and .дети Domains) 


## Parsing: 

Code: parse.py

Author: Ke and Prakhar

## Results:

```python 
The results are saved into pickle data for performance. A pickle data is a set of unique domains.

ru: length of lines: 13331201, unique domains 5325230
[Pickle]: save object into ru.pickle

su: length of lines: 271326, unique domains 109718
[Pickle]: save object into su.pickle

tatar: length of lines: 2089, unique domains 869
[Pickle]: save object into tatar.pickle

дети: length of lines: 2557, unique domains 1067
[Pickle]: save object into дети.pickle


//Notice: the рф.zone is not in a good format! needs doublechekcing. 
рф: length of lines: 307, unique domains 296
[Pickle]: save object into рф.pickle
```

## Project and data site: /home/cuckoo/labdata/RussiaDNSLeak

```bash
100M	ru.pickle
1.9M	su.pickle
16K     tatar.pickle
36K     дети.pickle
16K     рф.pickle
```

Stored as a set, each element is a string for domain name.
```python
How to load: use pickle
>>> import pickle
>>> pickle.compatible_formats
['1.0', '1.1', '1.2', '1.3', '2.0']
```

## Summary
Due to an accidentally enabling of [global zone transfers](https://en.wikipedia.org/wiki/DNS_zone_transfer) on the Russian DNS nameservers `a.dns.ripn.net`, `d.dns.ripn.net`, and `f.dns.ripn.net` the [TLDR project](https://github.com/mandatoryprogrammer/TLDR) was able to capture a complete list of all domains registered under Russian TLD space. Russia has fixed this issue (possibly due to the problem [gaining traction after the TLDR project link was  posted to a Russian tech news aggregator](https://habrahabr.ru/post/331144/) by [@ValdikSS](https://twitter.com/ValdikSS)) so I am creating this repository to summarize the data collected due to this leak. Humorously the leak actually caused an outage for this TLDR service because the [leaked zone data was so large it killed the script attempting to collect it by filling up all available memory on the server](https://github.com/mandatoryprogrammer/TLDR/issues/11#issuecomment-309254675). This issue has now been fixed and the leaked DNS data is all backed up and hosted here for general consumption. The size of this dump is enormous compared to previous leaks such as the previously captured [North Korean DNS dump](https://github.com/mandatoryprogrammer/NorthKoreaDNSLeak), `.ru` domains alone account for over *[5.1% of all domain names on the Internet](https://w3techs.com/technologies/overview/top_level_domain/all)*.

### Number of Domain Names Leaked
* `.ru (Russia ccTLD)`: 5,214,868 domains.
* `.su (Soviet Union ccTLD)`: 104,591 domains.
* `.tatar ( gTLD)`: 861 domains.
* `.рф ( IDN ccTLD)`: 466,890 domains.
* `.дети ( gTLD)`: 821 domains.

Total domains: 5,788,031

### Downloads of Leaked Zone Data
* `.ru` Zone data: [Download here](https://github.com/mandatoryprogrammer/TLDR/blob/e04bef94efbf546760888b7608fee10e6639aede/archives/ru/a.dns.ripn.net.zone.gz?raw=true) (Compressed due to large size)
* `.su` Zone data: [Download here](https://raw.githubusercontent.com/mandatoryprogrammer/TLDR/e04bef94efbf546760888b7608fee10e6639aede/archives/su/a.dns.ripn.net.zone)
* `.tatar` Zone data: [Download here](https://raw.githubusercontent.com/mandatoryprogrammer/TLDR/e04bef94efbf546760888b7608fee10e6639aede/archives/tatar/a.dns.ripn.net.zone)
* `.рф` Zone data: [Download here](https://github.com/mandatoryprogrammer/TLDR/blob/e04bef94efbf546760888b7608fee10e6639aede/archives/xn--p1ai/a.dns.ripn.net.zone.gz?raw=true)
* `.дети` Zone data: [Download here](https://raw.githubusercontent.com/mandatoryprogrammer/TLDR/e04bef94efbf546760888b7608fee10e6639aede/archives/xn--d1acj3b/a.dns.ripn.net.zone)

Additionally this repository can be cloned in order to obtain a copy of all of these zone files.
