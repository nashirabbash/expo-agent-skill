---
title: "Progress Indicators"
description: "Jetpack Compose progress indicator components for displaying operation status."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/progress.md"
scraped_at: "2026-07-15T09:01:00.076868"
---

---
title: Progress Indicators
description: Jetpack Compose progress indicator components for displaying operation status.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Progress Indicators

Jetpack Compose progress indicator components for displaying operation status.
Android, Included in Expo Go

Expo UI Progress Indicators match the official Jetpack Compose [Progress Indicator API](https://developer.android.com/develop/ui/compose/components/progress).

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Linear progress

A horizontal bar that fills to indicate progress. Provide a `progress` value between `0` and `1` for determinate mode.

```tsx
import { Host, LinearProgressIndicator } from '@expo/ui/jetpack-compose';

export default function LinearExample() {
  return (
    <Host matchContents>
      <LinearProgressIndicator progress={0.5} />
    </Host>
  );
}
```

### Circular progress

A spinning circle whose stroke grows to indicate progress.

```tsx
import { Host, CircularProgressIndicator } from '@expo/ui/jetpack-compose';

export default function CircularExample() {
  return (
    <Host matchContents>
      <CircularProgressIndicator progress={0.75} />
    </Host>
  );
}
```

### Indeterminate

Omit the `progress` prop to animate continuously without indicating a specific completion level.

```tsx
import {
  CircularProgressIndicator,
  CircularWavyProgressIndicator,
  Column,
  Host,
  LinearProgressIndicator,
  LinearWavyProgressIndicator,
} from '@expo/ui/jetpack-compose';

export default function IndeterminateExample() {
  return (
    <Host matchContents>
      <Column verticalArrangement={{ spacedBy: 16 }}>
        <LinearProgressIndicator />
        <CircularProgressIndicator />
        <CircularWavyProgressIndicator />
        <LinearWavyProgressIndicator />
      </Column>
    </Host>
  );
}
```

### Custom colors

Use `color` for the indicator and `trackColor` for the background track.

```tsx
import { Host, CircularProgressIndicator } from '@expo/ui/jetpack-compose';

export default function ColorsExample() {
  return (
    <Host matchContents>
      <CircularProgressIndicator progress={0.6} color="red" trackColor="#cccccc" />
    </Host>
  );
}
```

### Wavy variants

`LinearWavyProgressIndicator` and `CircularWavyProgressIndicator` add an expressive wave animation from Material 3 Expressive.

```tsx
import {
  Host,
  LinearWavyProgressIndicator,
  CircularWavyProgressIndicator,
  Column,
} from '@expo/ui/jetpack-compose';

export default function WavyExample() {
  return (
    <Host matchContents>
      <Column verticalArrangement={{ spacedBy: 16 }}>
        <LinearWavyProgressIndicator progress={0.6} />
        <CircularWavyProgressIndicator progress={0.6} />
      </Column>
    </Host>
  );
}
```

## API

```tsx
import {
  LinearProgressIndicator,
  CircularProgressIndicator,
  LinearWavyProgressIndicator,
  CircularWavyProgressIndicator,
} from '@expo/ui/jetpack-compose';
```

## Components

### `CircularProgressIndicator`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[CircularProgressIndicatorProps](#circularprogressindicatorprops)\>\>

A circular progress indicator that displays progress in a circular format.

Matches the Jetpack Compose `CircularProgressIndicator`.

Common props shared by all progress indicator variants.

CircularProgressIndicatorProps

### `gapSize`

Supported platforms: Android.

Optional • Type: `number`

Gap size between the indicator and track in dp.

### `strokeCap`

Supported platforms: Android.

Optional • Type: [StrokeCap](#strokecap) • Default: `'round'`

Stroke cap style for the indicator ends.

### `strokeWidth`

Supported platforms: Android.

Optional • Type: `number`

Width of the circular stroke in dp.

#### Inherited Props

-   [ProgressCommonConfig](#progresscommonconfig)

### `CircularWavyProgressIndicator`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[CircularWavyProgressIndicatorProps](#circularwavyprogressindicatorprops)\>\>

A circular progress indicator with wavy animation style.

Matches the Jetpack Compose `CircularWavyProgressIndicator`.

Common props shared by all progress indicator variants.

CircularWavyProgressIndicatorProps

#### Inherited Props

-   [ProgressCommonConfig](#progresscommonconfig)

### `LinearProgressIndicator`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[LinearProgressIndicatorProps](#linearprogressindicatorprops)\>\>

A linear progress indicator that displays progress in a horizontal bar.

Matches the Jetpack Compose `LinearProgressIndicator`.

Common props shared by all progress indicator variants.

LinearProgressIndicatorProps

### `drawStopIndicator`

Supported platforms: Android.

Optional • Type: [DrawStopIndicatorConfig](#drawstopindicatorconfig)

Configuration for the stop indicator dot at the end of the determinate progress track.

### `gapSize`

Supported platforms: Android.

Optional • Type: `number`

Gap size between the indicator and track in dp.

### `strokeCap`

Supported platforms: Android.

Optional • Type: [StrokeCap](#strokecap) • Default: `'round'`

Stroke cap style for the indicator ends.

#### Inherited Props

-   [ProgressCommonConfig](#progresscommonconfig)

### `LinearWavyProgressIndicator`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[LinearWavyProgressIndicatorProps](#linearwavyprogressindicatorprops)\>\>

A linear progress indicator with wavy animation style.

Matches the Jetpack Compose `LinearWavyProgressIndicator`.

Common props shared by all progress indicator variants.

LinearWavyProgressIndicatorProps

### `stopSize`

Supported platforms: Android.

Optional • Type: `number`

Size of the stop indicator in dp at the end of the determinate progress track.

#### Inherited Props

-   [ProgressCommonConfig](#progresscommonconfig)

## Types

### `DrawStopIndicatorConfig`

Supported platforms: Android.

Configuration for the stop indicator dot at the end of the determinate linear progress track. When provided, draws a stop indicator with the given options. Omit to use the Compose default.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Color of the stop indicator. Defaults to the indicator's color. |
| stopSize(optional) | `number` | Size of the stop indicator in dp. Defaults to the Material 3 default. |
| strokeCap(optional) | [StrokeCap](#strokecap) | Stroke cap style for the stop indicator. Defaults to the indicator's strokeCap. |

### `ProgressCommonConfig`

Supported platforms: Android.

Common props shared by all progress indicator variants.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Progress indicator color. |
| modifiers(optional) | `ModifierConfig[]` | Modifiers for the component. |
| progress(optional) | `number | null` | The current progress value between `0` and `1`. Omit for indeterminate. |
| trackColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Track (background) color. |

### `StrokeCap`

Supported platforms: Android.

Literal Type: `string`

Stroke cap style for progress indicators.

Acceptable values are: `'round'` | `'butt'` | `'square'`
