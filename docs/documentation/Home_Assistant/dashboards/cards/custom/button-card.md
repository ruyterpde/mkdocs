bar

``` yaml

type: custom:button-card
entity: sensor.home_assistant_host_disk_used
name: STORAGE USED
show_icon: false
show_state: true
tab_action:
  action: more-info
styles:
  card:
    - height: 80px
    - padding: 0px
    - border-radius: 10px
    - border: 1px solid
    - border-color: "#888888"
    - background: |
        [[[
          let value = (entity.state);
          if (value < 60) return 'linear-gradient(to right, #43A047 ' + value + '%, #434954 ' + value + '%)';
          if (value < 85) return 'linear-gradient(to right, #FFA600 ' + value + '%, #434954 ' + value + '%)';          
          return 'linear-gradient(to right, #DB4437 ' + value + '%, #434954 ' + value + '%)';
        ]]]
  name:
    - justify-self: start
    - padding-left: 30px
    - font-size: 14px
    - color: white
  state:
    - justify-self: start
    - padding-left: 30px
    - font-size: 14px
    - color: white

```
