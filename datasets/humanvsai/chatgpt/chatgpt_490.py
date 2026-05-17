def partner_iterator(partners, category):
    for partner in partners:
        if partner['category'] == category:
            yield partner
