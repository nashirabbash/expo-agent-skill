---
title: "Pedometer"
description: "A library that provides access to the device's pedometer sensor."
source_url: "https://docs.expo.dev/versions/latest/sdk/pedometer.md"
scraped_at: "2026-07-15T08:44:44.738749"
---

---
title: Pedometer
description: A library that provides access to the device's pedometer sensor.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-sensors'
packageName: 'expo-sensors'
iconUrl: '/static/images/packages/expo-sensors.png'
platforms: ['android', 'ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Expo Pedometer

A library that provides access to the device's pedometer sensor.
Android, iOS, Included in Expo Go

`Pedometer` from `expo-sensors` uses the system `hardware.Sensor` on Android and Core Motion on iOS to get the user's step count, and also allows you to subscribe to pedometer updates.

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
import { StyleSheet, Text, View } from 'react-native';
import { Pedometer } from 'expo-sensors';

export default function App() {
  const [isPedometerAvailable, setIsPedometerAvailable] = useState('checking');
  const [pastStepCount, setPastStepCount] = useState(0);
  const [currentStepCount, setCurrentStepCount] = useState(0);

  const subscribe = async () => {
    const isAvailable = await Pedometer.isAvailableAsync();
    setIsPedometerAvailable(String(isAvailable));

    if (isAvailable) {
      const end = new Date();
      const start = new Date();
      start.setDate(end.getDate() - 1);

      const pastStepCountResult = await Pedometer.getStepCountAsync(start, end);
      if (pastStepCountResult) {
        setPastStepCount(pastStepCountResult.steps);
      }

      return Pedometer.watchStepCount(result => {
        setCurrentStepCount(result.steps);
      });
    }
  };

  useEffect(() => {
    const subscription = subscribe();
    return () => subscription && subscription.remove();
  }, []);

  return (
    <View style={styles.container}>
      <Text>Pedometer.isAvailableAsync(): {isPedometerAvailable}</Text>
      <Text>Steps taken in the last 24 hours: {pastStepCount}</Text>
      <Text>Walk! And watch this go up: {currentStepCount}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 15,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

## API

```js
import { Pedometer } from 'expo-sensors';
```

## Methods

### `Pedometer.getPermissionsAsync()`

Supported platforms: Android, iOS.

Checks user's permissions for accessing pedometer.

Returns: `Promise<permissionresponse>`

### `Pedometer.getStepCountAsync(start, end)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `start` | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | A date indicating the start of the range over which to measure steps. |
| `end` | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | A date indicating the end of the range over which to measure steps. |

  

Get the step count between two dates.

Returns: `Promise<pedometerresult>`

Returns a promise that fulfills with a [`PedometerResult`](#pedometerresult).

As [Apple documentation states](https://developer.apple.com/documentation/coremotion/cmpedometer/1613946-querypedometerdatafromdate?language=objc):

> Only the past seven days worth of data is stored and available for you to retrieve. Specifying a start date that is more than seven days in the past returns only the available data.

### `Pedometer.isAvailableAsync()`

Supported platforms: Android, iOS.

Returns whether the pedometer is enabled on the device.

Returns: `Promise<boolean>`

Returns a promise that fulfills with a `boolean`, indicating whether the pedometer is available on this device.

### `Pedometer.requestPermissionsAsync()`

Supported platforms: Android, iOS.

Asks the user to grant permissions for accessing pedometer.

Returns: `Promise<permissionresponse>`

### `Pedometer.watchStepCount(callback)`

Supported platforms: Android, iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | [PedometerUpdateCallback](#pedometerupdatecallback) | A callback that is invoked when new step count data is available. The callback is provided with a single argument that is [`PedometerResult`](#pedometerresult). |

  

Subscribe to pedometer updates.

Returns: `EventSubscription`

Returns a [`Subscription`](#subscription) that enables you to call `remove()` when you would like to unsubscribe the listener.

> Pedometer updates will not be delivered while the app is in the background. As an alternative, on Android, use another solution based on [`Health Connect API`](https://developer.android.com/health-and-fitness/guides/health-connect). On iOS, the `getStepCountAsync` method can be used to get the step count between two dates.

## Interfaces

### `Subscription`

Supported platforms: Android, iOS.

A subscription object that allows to conveniently remove an event listener from the emitter.

Subscription Methods

### `remove()`

Supported platforms: Android, iOS.

Removes an event listener for which the subscription has been created. After calling this function, the listener will no longer receive any events from the emitter.

Returns: `void`

## Types

### `PedometerResult`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| steps | `number` | Number of steps taken between the given dates. |

### `PedometerUpdateCallback(result)`

Supported platforms: Android, iOS.

Callback function providing event result as an argument.

| Parameter | Type |
| --- | --- |
| `result` | [PedometerResult](#pedometerresult) |

Returns:

`void`

### `PermissionExpiration`

Supported platforms: Android, iOS.

Literal Type: `union`

Permission expiration time. Currently, all permissions are granted permanently.

Acceptable values are: `'never'` | `number`

### `PermissionResponse`

Supported platforms: Android, iOS.

An object obtained by permissions get and request functions.

| Property | Type | Description |
| --- | --- | --- |
| canAskAgain | `boolean` | Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission. |
| expires | `PermissionExpiration` | Determines time when the permission expires. |
| granted | `boolean` | A convenience boolean that indicates if the permission is granted. |
| status | [PermissionStatus](#permissionstatus) | Determines the status of the permission. |

## Enums

### `PermissionStatus`

Supported platforms: Android, iOS.

#### `DENIED`

`PermissionStatus.DENIED = "denied"`

User has denied the permission.

#### `GRANTED`

`PermissionStatus.GRANTED = "granted"`

User has granted the permission.

#### `UNDETERMINED`

`PermissionStatus.UNDETERMINED = "undetermined"`

User hasn't granted or denied the permission yet.
