---
title: "LightSensor"
description: "A library that provides access to the device's light sensor."
source_url: "https://docs.expo.dev/versions/latest/sdk/light-sensor.md"
scraped_at: "2026-07-15T08:43:50.955966"
---

---
title: LightSensor
description: A library that provides access to the device's light sensor.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-sensors'
packageName: 'expo-sensors'
iconUrl: '/static/images/packages/expo-sensors.png'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Expo LightSensor

A library that provides access to the device's light sensor.
Android, Included in Expo Go

`LightSensor` from `expo-sensors` provides access to the device's light sensor to respond to illuminance changes.

## Installation

```sh
# npm
npx expo install expo-sensors

# yarn
yarn expo install expo-sensors

# pnpm
pnpm expo install expo-sensors

# bun
bun expo install expo-sensors
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

```jsx
import { useState, useEffect } from 'react';
import { StyleSheet, Text, TouchableOpacity, View, Platform } from 'react-native';
import { LightSensor } from 'expo-sensors';

export default function App() {
  const [{ illuminance }, setData] = useState({ illuminance: 0 });
  const [subscription, setSubscription] = useState(null);

  const toggle = () => {
    if (subscription) {
      unsubscribe();
    } else {
      subscribe();
    }
  };

  const subscribe = () => {
    setSubscription(
      LightSensor.addListener(sensorData => {
        setData(sensorData);
      })
    );
  };

  const unsubscribe = () => {
    subscription && subscription.remove();
    setSubscription(null);
  };

  useEffect(() => {
    subscribe();
    return () => unsubscribe();
  }, []);

  return (
    <View style={styles.sensor}>
      <Text>Light Sensor:</Text>
      <Text>
        Illuminance: {Platform.OS === 'android' ? `${illuminance} lx` : `Only available on Android`}
      </Text>
      <View style={styles.buttonContainer}>
        <TouchableOpacity onPress={toggle} style={styles.button}>
          <Text>Toggle</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  sensor: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 10,
  },
  buttonContainer: {
    flexDirection: 'row',
    alignItems: 'stretch',
    marginTop: 15,
  },
  button: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#eee',
    padding: 10,
  },
});
```

## API

```js
import { LightSensor } from 'expo-sensors';
```

## Classes

### `LightSensor`

Supported platforms: Android.

Type: Class extends [DeviceSensor](/versions/latest/sdk/sensors.md)<[LightSensorMeasurement](#lightsensormeasurement)\>

LightSensor Methods

### `addListener(listener)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `listener` | Listener<[LightSensorMeasurement](#lightsensormeasurement)\> | A callback that is invoked when a LightSensor update is available. When invoked, the listener is provided a single argument that is the illuminance value. |

  

Subscribe for updates to the light sensor.

Returns: `EventSubscription`

A subscription that you can call `remove()` on when you would like to unsubscribe the listener.

### `getListenerCount()`

Supported platforms: Android.

Returns the registered listeners count.

Returns: `number`

### `getPermissionsAsync()`

Supported platforms: Android.

Checks user's permissions for accessing sensor.

Returns: `Promise<permissionresponse>`

### `hasListeners()`

Supported platforms: Android.

Returns boolean which signifies if sensor has any listeners registered.

Returns: `boolean`

### `isAvailableAsync()`

Supported platforms: Android.

> You should always check the sensor availability before attempting to use it.

Returns whether the light sensor is available and enabled on the device. Requires at least Android 2.3 (API Level 9).

Returns: `Promise<boolean>`

A promise that resolves to a `boolean` denoting the availability of the light sensor.

### `removeAllListeners()`

Supported platforms: Android.

Removes all registered listeners.

Returns: `void`

> **Deprecated:** use subscription.remove() instead.

### `removeSubscription(subscription)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `subscription` | `EventSubscription` |

  

Returns: `void`

### `requestPermissionsAsync()`

Supported platforms: Android.

Asks the user to grant permissions for accessing sensor.

Returns: `Promise<permissionresponse>`

### `setUpdateInterval(intervalMs)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `intervalMs` | `number` | Desired interval in milliseconds between sensor updates. Starting from Android 12 (API level 31), the system has a 200Hz limit for each sensor updates. |

  

Set the sensor update interval.

Returns: `void`

## Interfaces

### `Subscription`

Supported platforms: Android.

A subscription object that allows to conveniently remove an event listener from the emitter.

Subscription Methods

### `remove()`

Supported platforms: Android.

Removes an event listener for which the subscription has been created. After calling this function, the listener will no longer receive any events from the emitter.

Returns: `void`

## Types

### `LightSensorMeasurement`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| illuminance | `number` | Ambient light level registered by the device measured in lux (lx). |
| timestamp | `number` | Timestamp of the measurement in seconds. |

### `PermissionExpiration`

Supported platforms: Android.

Literal Type: `union`

Permission expiration time. Currently, all permissions are granted permanently.

Acceptable values are: `'never'` | `number`

### `PermissionResponse`

Supported platforms: Android.

An object obtained by permissions get and request functions.

| Property | Type | Description |
| --- | --- | --- |
| canAskAgain | `boolean` | Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission. |
| expires | `PermissionExpiration` | Determines time when the permission expires. |
| granted | `boolean` | A convenience boolean that indicates if the permission is granted. |
| status | [PermissionStatus](#permissionstatus) | Determines the status of the permission. |

## Enums

### `PermissionStatus`

Supported platforms: Android.

#### `DENIED`

`PermissionStatus.DENIED = "denied"`

User has denied the permission.

#### `GRANTED`

`PermissionStatus.GRANTED = "granted"`

User has granted the permission.

#### `UNDETERMINED`

`PermissionStatus.UNDETERMINED = "undetermined"`

User hasn't granted or denied the permission yet.
