---
title: "BottomSheet"
description: "A bottom sheet compatible with @gorhom/bottom-sheet."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/drop-in-replacements/bottomsheet.md"
scraped_at: "2026-07-15T08:46:00.103472"
---

---
title: BottomSheet
description: A bottom sheet compatible with @gorhom/bottom-sheet.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# BottomSheet

A bottom sheet compatible with @gorhom/bottom-sheet.
Android, iOS, Web, Included in Expo Go

A `BottomSheet` component with an API compatible with `@gorhom/bottom-sheet`. It wraps the platform-specific `@expo/ui` primitives: [Jetpack Compose ModalBottomSheet](/versions/latest/sdk/ui/jetpack-compose/bottomsheet.md) on Android and [SwiftUI BottomSheet](/versions/latest/sdk/ui/swift-ui/bottomsheet.md) on iOS. On web, it uses a [vaul](https://github.com/emilkowalski/vaul) drawer.

If you need lower-level control over platform-specific styling, modifiers, or layout behavior, use the native primitives directly.

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

## Migrating from `@gorhom/bottom-sheet`

-   Update imports from:
    
    ```tsx
    import BottomSheet, { BottomSheetView } from '@gorhom/bottom-sheet';
    ```
    
    To use `@expo/ui/community/bottom-sheet`:
    
    ```tsx
    import BottomSheet, { BottomSheetView } from '@expo/ui/community/bottom-sheet';
    ```
    
-   `GestureHandlerRootView` from `react-native-gesture-handler` is not required by this implementation. You can leave it in place if other parts of your app need it.
    
-   Component and hook exports such as `BottomSheetBackdrop`, `BottomSheetHandle`, `BottomSheetFooter`, `BottomSheetDraggableView`, `BottomSheetVirtualizedList`, `BottomSheetFlashList`, `useBottomSheetModal`, `useBottomSheetSpringConfigs`, and `useBottomSheetTimingConfigs` are not supported. Some related prop types are exported for API compatibility.
    

## Basic usage

```tsx
import { useRef } from 'react';
import { Button, Text, View } from 'react-native';
import BottomSheet, { BottomSheetView } from '@expo/ui/community/bottom-sheet';

export default function BottomSheetExample() {
  const sheetRef = useRef<BottomSheet>(null);

  return (
    <View style={{ flex: 1 }}>
      <Button title="Open" onPress={() => sheetRef.current?.snapToIndex(0)} />

      <BottomSheet
        ref={sheetRef}
        snapPoints={['25%', '50%', '90%']}
        index={-1}
        onChange={index => {
          console.log('onChange', index);
        }}
        onClose={() => {
          console.log('closed');
        }}
        enablePanDownToClose>
        <BottomSheetView style={{ flex: 1, padding: 24, alignItems: 'center' }}>
          <Text>Sheet content</Text>
        </BottomSheetView>
      </BottomSheet>
    </View>
  );
}
```

## `BottomSheetModal`

Use `BottomSheetModal` when migrating from `@gorhom/bottom-sheet` modal APIs. It starts closed and opens with `present()`.

```tsx
import { useRef } from 'react';
import { Button, Text, View } from 'react-native';
import { BottomSheetModal, BottomSheetView } from '@expo/ui/community/bottom-sheet';

export default function BottomSheetModalExample() {
  const modalRef = useRef<BottomSheetModal>(null);

  return (
    <View style={{ flex: 1 }}>
      <Button title="Present" onPress={() => modalRef.current?.present()} />

      <BottomSheetModal ref={modalRef} snapPoints={['50%', '90%']} enablePanDownToClose>
        <BottomSheetView style={{ padding: 24 }}>
          <Text>Modal content</Text>
          <Button title="Dismiss" onPress={() => modalRef.current?.dismiss()} />
        </BottomSheetView>
      </BottomSheetModal>
    </View>
  );
}
```

## Dynamic sizing

When `snapPoints` is not provided, the sheet sizes to fit its content by default. Use `BottomSheetView` for the sheet content wrapper.

```tsx
import { useRef } from 'react';
import { Button, Text, View } from 'react-native';
import BottomSheet, { BottomSheetView } from '@expo/ui/community/bottom-sheet';

export default function DynamicBottomSheetExample() {
  const sheetRef = useRef<BottomSheet>(null);

  return (
    <View style={{ flex: 1 }}>
      <Button title="Open" onPress={() => sheetRef.current?.present()} />

      <BottomSheet ref={sheetRef} index={-1} enablePanDownToClose>
        <BottomSheetView style={{ padding: 24 }}>
          <Text>This sheet sizes itself to its content.</Text>
        </BottomSheetView>
      </BottomSheet>
    </View>
  );
}
```

## Platform behavior

`@gorhom/bottom-sheet` renders inline at the bottom of its parent view. This component uses native modal presentation on Android and iOS, and a drawer overlay on web.

This difference is intentional. `@gorhom/bottom-sheet` owns the gesture and animation layer through `react-native-gesture-handler` and `react-native-reanimated`, while `@expo/ui/community/bottom-sheet` delegates those behaviors to Jetpack Compose, SwiftUI, and the web drawer primitive. As a result, this component is best suited for modal bottom sheet flows, including callsites that use the `BottomSheet` API rather than `BottomSheetModal`.

| Feature | Android | iOS | Web |
| --- | --- | --- | --- |
| Presentation | Jetpack Compose modal bottom sheet | SwiftUI sheet | vaul drawer |
| Snap points | Maps to partial and expanded states | Supports provided snap points | Supports provided snap points |
| No `snapPoints` | Fits content | Fits content | Fits content |
| Pan down to close | Also enables back button and scrim tap dismiss | Also enables backdrop tap dismiss | Enables drawer dismiss |
| Persistent inline peek | Not supported | Not supported | Not supported |

## Supported exports

| Export | Supported | Notes |
| --- | --- | --- |
| `BottomSheet` | ✓ | Modal on Android and iOS, drawer on web |
| `BottomSheetModal` | ✓ | Starts closed and opens with `present()` |
| `BottomSheetModalProvider` | ✓ | Renders children directly for compatibility |
| `BottomSheetView` | ✓ | Wraps sheet content |
| `BottomSheetScrollView` | ✓ | Re-export of React Native `ScrollView` |
| `BottomSheetFlatList` | ✓ | Re-export of React Native `FlatList` |
| `BottomSheetSectionList` | ✓ | Re-export of React Native `SectionList` |
| `BottomSheetTextInput` | ✓ | Re-export of React Native `TextInput` |
| `useBottomSheet` | ✓ | Returns the sheet ref methods from context |
| `BottomSheetBackdrop` | ✗ | The native sheet or web drawer handles the backdrop |
| `BottomSheetHandle` | ✗ | The native sheet or web drawer handles the drag indicator |
| `BottomSheetFooter` | ✗ | No equivalent in this implementation |

## Compatibility notes

-   `snapPoints`, `index`, `onChange`, `onClose`, `onDismiss`, `enablePanDownToClose`, and `enableDynamicSizing` are supported.
-   `handleComponent={null}` hides the native or web drag indicator. Custom handle components are not rendered on native platforms.
-   `backgroundStyle` applies fully on web. On Android, `backgroundColor` is used for the native container color. On iOS, the system sheet background is used.
-   Animation, over-drag, content panning, handle panning, keyboard behavior, custom backdrop, custom background, custom footer, animated value, and detached props are accepted for API compatibility but do not change behavior.

## API

```tsx
import BottomSheet from '@expo/ui/community/bottom-sheet';
```

## Components

### `BottomSheet`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BottomSheetProps](#bottomsheetprops)\>

Bottom sheet component. Defaults to `index={0}` and opens at the first snap point on mount.

Props for the `BottomSheet` component. API-compatible with `@gorhom/bottom-sheet` where native platform behavior allows.

BottomSheetProps

### `children`

Supported platforms: Android, iOS, Web.

Type: `React.ReactNode`

The content to render inside the bottom sheet.

### `enableDynamicSizing`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `true`

Whether the sheet should automatically size to fit its content.

### `enablePanDownToClose`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the sheet can be dismissed by panning down.

### `index`

Supported platforms: Android, iOS, Web.

Optional • Type: `number` • Default: `0`

Initial snap point index. Set to -1 to start closed.

### `onChange`

Supported platforms: Android, iOS, Web.

Optional • Type: `(index: number) => void`

Called when the current snap point index changes.

### `onClose`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the bottom sheet is fully closed.

### `onDismiss`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Alias for `onClose` for `BottomSheetModal` compatibility.

### `snapPoints`

Supported platforms: Android, iOS, Web.

Optional • Type: `(string | number)[]`

Points for the bottom sheet to snap to, ordered from bottom to top.

### `BottomSheetModal`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BottomSheetProps](#bottomsheetprops)\>

Modal variant of `BottomSheet`. Starts closed and opens with `present()`.

### `BottomSheetModalProvider`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<{ children: React.ReactNode }\>

Provider for `BottomSheetModal`. It renders children directly for API compatibility.

### `BottomSheetView`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BottomSheetViewProps](#bottomsheetviewprops)\>

A wrapper for content inside a `BottomSheet`.

Props for the `BottomSheetView` content wrapper.

BottomSheetViewProps

### `children`

Supported platforms: Android, iOS, Web.

Type: `React.ReactNode`

The content to render inside the bottom sheet.

### `enableDynamicSizing`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `true`

Whether the sheet should automatically size to fit its content.

### `enablePanDownToClose`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the sheet can be dismissed by panning down.

### `index`

Supported platforms: Android, iOS, Web.

Optional • Type: `number` • Default: `0`

Initial snap point index. Set to -1 to start closed.

### `onChange`

Supported platforms: Android, iOS, Web.

Optional • Type: `(index: number) => void`

Called when the current snap point index changes.

### `onClose`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the bottom sheet is fully closed.

### `onDismiss`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Alias for `onClose` for `BottomSheetModal` compatibility.

### `snapPoints`

Supported platforms: Android, iOS, Web.

Optional • Type: `(string | number)[]`

Points for the bottom sheet to snap to, ordered from bottom to top.

### `children`

Supported platforms: Android, iOS, Web.

Type: `React.ReactNode`

## Hooks

### `useBottomSheet()`

Supported platforms: Android, iOS, Web.

Returns the imperative methods for the nearest `BottomSheet`.

Returns: `BottomSheetMethods`

## Types

### `BottomSheetMethods`

Supported platforms: Android, iOS, Web.

Imperative methods exposed by `BottomSheet` and `BottomSheetModal` refs.

| Property | Type | Description |
| --- | --- | --- |
| close | `() => void` | Close the bottom sheet. |
| collapse | `() => void` | Snap to the minimum snap point. |
| dismiss | `() => void` | Dismiss the bottom sheet. |
| expand | `() => void` | Snap to the maximum snap point. |
| forceClose | `() => void` | Force close the bottom sheet. |
| present | `() => void` | Present the bottom sheet at the first snap point. |
| snapToIndex | `(index: number) => void` | Snap to a snap point by index. |
| snapToPosition | `(position: string | number) => void` | Snap to a pixel value or percentage position. |
