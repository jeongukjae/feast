# Feature view

## Feature View

A feature view is an object that represents a logical group of time-series feature data as it is found in a [data source](data-source.md). Feature views consist of zero or more [entities](entity.md), one or more [features](feature-view.md#feature), and a [data source](data-source.md). Feature views allow Feast to model your existing feature data in a consistent way in both an offline \(training\) and online \(serving\) environment. If a feature view contains features that are properties of a specific object, that object is typically defined as an entity and included in the feature view. If a feature view contains features that are not related to a specific entity, for example global features, the feature view can be defined without entities.

{% tabs %}
{% tab title="driver\_trips\_feature\_view.py" %}
```python
driver_stats_fv = FeatureView(
    name="driver_activity",
    entities=["driver"],
    features=[
        Feature(name="trips_today", dtype=ValueType.INT64),
        Feature(name="rating", dtype=ValueType.FLOAT),
    ],
    batch_source=BigQuerySource(
        table_ref="feast-oss.demo_data.driver_activity"
    )
)
```
{% endtab %}

{% tab title="global\_feature\_view.py" %}
```python
global_stats_fv = FeatureView(
    name="global_stats",
    entities=[],
    features=[
        Feature(name="total_trips_today", dtype=ValueType.INT64),
    ],
    batch_source=BigQuerySource(
        table_ref="feast-oss.demo_data.global_stats"
    )
)
```
{% endtab %}
{% endtabs %}

Feature views are used during

* The generation of training datasets by querying the data source of feature views in order to find historical feature values. A single training dataset may consist of features from multiple feature views.
* Loading of feature values into an online store. Feature views determine the storage schema in the online store.
* Retrieval of features from the online store. Feature views provide the schema definition to Feast in order to look up features from the online store.

{% hint style="info" %}
Feast does not generate feature values. It acts as the ingestion and serving system. The data sources described within feature views should reference feature values in their already computed form.
{% endhint %}

## Feature

A feature is an individual measurable property. It is typically a property observed on a specific entity, but does not have to be associated with an entity. For example, a feature of a `customer` entity could be the number of transactions they have made on an average month, while a feature that is not observed on a specific entity could be the total number of posts made by all users in the last month.

Features are defined as part of feature views. Since Feast does not transform data, a feature is essentially a schema that only contains a name and a type:

```python
trips_today = Feature(
    name="trips_today",
    dtype=ValueType.FLOAT
)
```

Together with [data sources](data-source.md), they indicate to Feast where to find your feature values, e.g., in a specific parquet file or BigQuery table. Feature definitions are also used when reading features from the feature store, using [feature references](feature-retrieval.md#feature-references).

Feature names must be unique within a [feature view](feature-view.md#feature-view).
