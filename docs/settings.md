# Custom Settings

## In Config

```
{
  "ParamPersistance": 60
}
```

| Setting          | Description                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------------- |
| ParamPersistance | Determines how long interactions will continue to populate in the chatbox since the last time it was triggered. |

## In Tracker

```
{
  "Headpats": {
    "current_count": 12341,
    "last_count": 12341,
    "last_activated": 1662804312.377652,
    "frequency_limit": 0
  }
}
```

| Setting         | Description                                                                                                                                                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Headpats"      | Name of the interaction. This is auto generated and is set by what you put as the parameter name in Unity. <br> Ex. This was set as `Track_Headpats` in Unity                                                                                              |
| current_count   | Most up to date count of interactions                                                                                                                                                                                                                         |
| last_count      | Count of interactions since last sent to VRC chatbox                                                                                                                                                                                                          |
| last_activated  | Time since interaction was last triggered                                                                                                                                                                                                                     |
| frequency_limit | Sets the delay till next interaction can be triggered for this contact in seconds. Defaults to `0 `meaning this interaction can be spammed. <br> Ex. If you want to limit the total number of interactions to 10 a second you would set this value to `0.10`. |
