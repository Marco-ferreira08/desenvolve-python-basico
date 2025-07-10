def criadorDominios(url):
    dominio = url[4:-10:]
    return dominio

URLs = ["www.google.com&quot;", "www.gmail.com&quot;", "www.github.com&quot;",  "www.reddit.com&quot;", "www.yahoo.com&quot;"]
URLs = [list(i) for i in URLs]
URLs = [criadorDominios(i) for i in URLs]
dominios = [''.join(i) for i in URLs]
print(dominios)