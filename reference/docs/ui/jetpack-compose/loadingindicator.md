---
title: "LoadingIndicator"
description: "Jetpack Compose loading indicator components for displaying loading state."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/loadingindicator.md"
scraped_at: "2026-07-15T09:00:53.807794"
---

---
title: LoadingIndicator
description: Jetpack Compose loading indicator components for displaying loading state.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# LoadingIndicator

Jetpack Compose loading indicator components for displaying loading state.
Android, Included in Expo Go

Expo UI Loading Indicators match the official Jetpack Compose [Loading Indicator API](https://m3.material.io/components/loading-indicator/overview).

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

### Loading indicator

A morphing-shape loading animation from Material 3 Expressive.

```tsx
import { Host, LoadingIndicator } from '@expo/ui/jetpack-compose';

export default function LoadingIndicatorExample() {
  return (
    <Host matchContents>
      <LoadingIndicator />
    </Host>
  );
}
```

### Contained loading indicator

A loading indicator inside a colored background.

```tsx
import { Host, ContainedLoadingIndicator } from '@expo/ui/jetpack-compose';

export default function ContainedLoadingIndicatorExample() {
  return (
    <Host matchContents>
      <ContainedLoadingIndicator />
    </Host>
  );
}
```

### Indeterminate

Omit the `progress` prop to animate continuously without indicating a specific completion level.

```tsx
import { ContainedLoadingIndicator, Host, LoadingIndicator, Row } from '@expo/ui/jetpack-compose';

export default function IndeterminateExample() {
  return (
    <Host matchContents>
      <Row horizontalArrangement={{ spacedBy: 16 }}>
        <LoadingIndicator />
        <ContainedLoadingIndicator />
      </Row>
    </Host>
  );
}
```

### Determinate

Pass an observable state from `useNativeState` as `progress`. Update `progress.value` between `0` and `1`.

```tsx
import {
  ContainedLoadingIndicator,
  Host,
  LoadingIndicator,
  Row,
  useNativeState,
} from '@expo/ui/jetpack-compose';
import { useEffect } from 'react';

export default function DeterminateExample() {
  const progress = useNativeState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      progress.value = (progress.value + 0.05) % 1;
    }, 500);
    return () => clearInterval(interval);
  }, [progress]);

  return (
    <Host matchContents>
      <Row horizontalArrangement={{ spacedBy: 16 }}>
        <LoadingIndicator progress={progress} />
        <ContainedLoadingIndicator progress={progress} />
      </Row>
    </Host>
  );
}
```

## API

```tsx
import { LoadingIndicator, ContainedLoadingIndicator } from '@expo/ui/jetpack-compose';
```

## Components

### `ContainedLoadingIndicator`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[ContainedLoadingIndicatorProps](#containedloadingindicatorprops)\>\>

A loading indicator that displays loading using morphing shapes inside a container.

Matches the Jetpack Compose `ContainedLoadingIndicator`.

Common props shared by loading indicator variants.

ContainedLoadingIndicatorProps

### `containerColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Loading indicator's container color

#### Inherited Props

-   [LoadingIndicatorCommonConfig](#loadingindicatorcommonconfig)

### `LoadingIndicator`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[LoadingIndicatorCommonConfig](#loadingindicatorcommonconfig)\>\>

A loading indicator that displays loading using morphing shapes.

Matches the Jetpack Compose `LoadingIndicator`.

## Types

### `LoadingIndicatorCommonConfig`

Supported platforms: Android.

Common props shared by loading indicator variants.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Loading indicator color. |
| modifiers(optional) | `ModifierConfig[]` | Modifiers for the component. |
| progress(optional) | [ObservableState](#observablestate)<number | null\> | An observable state that holds the current progress value. Create one with `useNativeState(0)`. Omit for indeterminate loading. |

### `ObservableState`

Supported platforms: Android.

Observable state shared between JavaScript and native views (Jetpack Compose on Android and SwiftUI on iOS).

Type: [SharedObject](/versions/v57.0.0/sdk/expo.md#sharedobjecttype) extended by:

| Property | Type | Description |
| --- | --- | --- |
| onChange | `[listener] | null` | A single listener invoked on the native UI runtime whenever the value changes (after iOS `didSet` and Android's setter). Assigning replaces the previous listener; assign `null` to clear. The initial value does not fire `onChange`. The callback must be a worklet so it can run synchronously on the UI thread. Attach it inside `useEffect` and clear it in the cleanup so the listener lifecycle matches the component lifecycle. . Example
```tsx
const state = useNativeState(0);

useEffect(() => {
  state.onChange = (value) => {
    'worklet';
    console.log('changed to', value);
  };
}, []);
```

 |
| value | `T` | The current value. Writes from a UI worklet are synchronous and immediately readable. Writes from the JS thread are scheduled to the UI thread asynchronously, the new value is not readable until the update has been applied. Prefer writing from a worklet when you need synchronous updates |
| get | `() => T` | Reads the current value. A React Compiler compliant alternative to reading `.value` |
| set | `(value: T) => void` | Writes a new value. A React Compiler-compliant alternative to assigning `.value` |
