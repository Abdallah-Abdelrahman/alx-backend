# Pagination

Most endpoints that return a list of entities will need to have some sort of pagination.

Without pagination, a simple search could return millions or even billions of hits causing extraneous network traffic.

Paging requires an implied ordering. By default this may be the item’s unique identifier, but can be other ordered fields such as a created date.

## Types of pagination:

- Offset Pagination
- Keyset Pagination
- Seek Pagination

## Learning Objectives:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner
