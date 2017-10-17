import collection
import analyze
import visualize

pagename = "jtbcnews"
since = '2017-10-01'
until = '2017-10-01'

if __name__ == '__main__':
    items = [
        {'pagename': 'jtbcnews', 'since': '2017-01-01', 'until': '2017-10-16'},
        {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-10-16'}
    ]

    # collection
    for item in items:
        resultfile = collection.crawling(**item)
        item['resultfile'] = resultfile

    # analysis
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count'] = analyze.count_wordfreq(data)

    # visualization
    for item in items:
        count = item['count']
        count_t50 = dict(count.most_common(50))
        filename = '%s_%s_%s.png' % (item['pagename'], item['since'], item['until'])
        visualize.graph_bar(
            values=list(count_t50.values()),
            ticks=list(count_t50.keys()),
            showgrid=True,
            filename=filename,
            showgraph=False
        )

